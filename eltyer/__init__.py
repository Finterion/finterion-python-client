import requests
import threading
from logging import getLogger
from multiprocessing.pool import ThreadPool

from eltyer.configuration.config import Config
from eltyer.configuration import constants
from eltyer.models import OrderSide, OrderType, Order, Position, Portfolio, \
    OrderStatus
from eltyer.exceptions import ClientException


logger = getLogger(__name__)


class Client:
    config = Config()
    thread_count = 2
    _pool = None

    # Algorithm specific attributes
    algorithm_id = None
    environment = None
    scheduler = None
    status = None

    def start(self):

        if not self.config.configured:
            raise ClientException("Client is not configured")

        algorithm_data = self._retrieve_algorithm()
        Client.algorithm_id = algorithm_data["algorithm_id"]
        Client.environment = algorithm_data["environment"]

        self.create_subscription()
        self.status = self.retrieve_subscription_status()

        t = threading.Timer(60, self.notify_online)
        t.daemon = True
        t.start()

    def create_subscription(self):

        payload = {}

        if self.config.CLOUD_FUNCTION:
            payload = {
                "cloud_function": True,
                "aws_function_name": self.config.AWS_FUNCTION_NAME,
                "time_unit": self.config.TIME_UNIT,
                "interval": self.config.INTERVAL
            }
        url = f"{constants.ORCHESTRATION_CREATION_ENDPOINT.format(algorithm_id=self.algorithm_id, environment=self.environment)}"

        response = requests.post(
            url, json=payload, headers={"x-api-key": self.config.API_KEY}
        )

        self._handle_response(response)

    def notify_online(self):
        url = f"{constants.ORCHESTRATION_ONLINE_ENDPOINT.format(algorithm_id=self.algorithm_id, environment=self.environment)}"

        response = requests.get(
            url, headers={"x-api-key": self.config.API_KEY}
        )

        self._handle_response(response)

    def retrieve_subscription_status(self):
        url = f"{constants.SUBSCRIPTION_STATUS.format(algorithm_id=self.algorithm_id, environment=self.environment)}"

        response = requests.get(
            url, headers={"x-api-key": self.config.API_KEY}
        )

        return self._handle_response(response)

    def stop(self):

        if self._pool:
            self._pool.close()
            self._pool.join()
            self._pool = None

    def get_environment(self):
        return self.environment

    @property
    def pool(self):
        if self._pool is None:
            self._pool = ThreadPool(self.thread_count)

        return self._pool

    def create_limit_order(
            self,
            target_symbol: str,
            price: float,
            amount: float,
            side: str = OrderSide.BUY.value,
            json=False
    ) -> Order:
        self.check_context()

        payload = {
            "target_symbol": target_symbol,
            "price": price,
            "amount": amount,
            "side": OrderSide.from_value(side).value,
            "type": OrderType.LIMIT.value,
        }

        response = requests.post(
            constants.ORDERS_ENDPOINT,
            json=payload,
            headers={"x-api-key": self.config.API_KEY}
        )

        data = self._handle_response(response)

        if json:
            return data

        return Order.from_dict(data)

    def create_market_order(
            self,
            target_symbol: str,
            amount: float,
            json=False
    ) -> Order:
        payload = {
            "target_symbol": target_symbol,
            "amount": amount,
            "side": OrderSide.SELL.value,
            "type": OrderType.MARKET.value,
        }

        response = requests.post(
            constants.ORDERS_ENDPOINT,
            json=payload,
            headers={"x-api-key": self.config.API_KEY}
        )

        data = self._handle_response(response)

        if json:
            return data

        return Order.from_dict(data)

    def get_orders(self, target_symbol: str = None, status=None, json=False):
        self.check_context()

        params = {}

        if target_symbol is not None:
            params["target_symbol"] = target_symbol

        if status is not None:
            params["status"] = OrderStatus.from_value(status)

        params["itemized"] = True

        response = requests.get(
            f"{constants.LIST_ORDERS_ENDPOINT.format(algorithm_id=self.algorithm_id)}",
            params=params,
            headers={"x-api-key": self.config.API_KEY}
        )

        data = self._handle_response(response)
        orders = []

        if json:
            return data["items"]

        for order_data in data["items"]:
            orders.append(Order.from_dict(order_data))

        return orders

    def get_order(self, reference_id, json=False) -> Order:
        response = requests.get(
            f"{constants.LIST_ORDERS_ENDPOINT.format(algorithm_id=self.algorithm_id)}",
            headers={"x-api-key": self.config.API_KEY}
        )

        data = self._handle_response(response)

        for order_data in data["items"]:
            ref_order = Order.from_dict(order_data)

            if ref_order.order_reference == reference_id:

                if json:
                    return order_data

                return ref_order

        return None

    def get_positions(self, json=False):
        self.check_context()

        portfolio = self.get_portfolio()

        unallocated_position = Position.from_dict(
            {
                "symbol": portfolio.trading_symbol,
                "amount": portfolio.unallocated
            }
        )

        response = requests.get(
            f"{constants.POSITIONS_ENDPOINT.format(algorithm_id=self.algorithm_id)}",
            params={"itemized": True},
            headers={"x-api-key": self.config.API_KEY}
        )

        data = self._handle_response(response)

        if json:
            positions = data["items"]
            positions.append(unallocated_position.to_dict())
            return positions

        # Add unallocated as a position
        positions = [
            Position.from_dict(
                {
                    "symbol": portfolio.trading_symbol,
                    "amount": portfolio.unallocated
                }
            )
        ]

        for position_data in data["items"]:
            positions.append(Position.from_dict(position_data))

        return positions

    def get_position(self, symbol: str, json=False):
        self.check_context()

        response = requests.get(
            f"{constants.POSITIONS_ENDPOINT.format(algorithm_id=self.algorithm_id)}",
            params={"itemized": True},
            headers={"x-api-key": self.config.API_KEY}
        )

        data = self._handle_response(response)

        for position_data in data["items"]:

            if position_data["symbol"].upper() == symbol.upper():

                if json:
                    return position_data

                return Position.from_dict(position_data)

        return None

    def get_portfolio(self, json=False):
        self.check_context()

        response = requests.get(
            f"{constants.PORTFOLIO_ENDPOINT.format(algorithm_id=self.algorithm_id)}",
            params={"itemized": True},
            headers={"x-api-key": self.config.API_KEY}
        )
        data = self._handle_response(response)

        if json:
            return data

        return Portfolio.from_dict(data)

    def _handle_response(self, response):

        if response.status_code >= 400:

            if response.status_code == 500:
                raise ClientException("Something went wrong at ELTYER")

            try:
                raise ClientException(response.json()["error_message"])
            except JSONDecodeError:
                raise ClientException("Something went wrong at ELTYER")

        return response.json()

    def _retrieve_algorithm(self):
        response = requests.get(
            f"{constants.API_KEY_VERIFY_ENDPOINT}",
            headers={"x-api-key": self.config.API_KEY}
        )

        return self._handle_response(response)

    def check_context(self):

        if self.algorithm_id is None:
            raise ClientException("Client is not configured")


__all__ = [
    "Client",
    "OrderType",
    "OrderStatus",
    "OrderSide",
    "ClientException"
]
