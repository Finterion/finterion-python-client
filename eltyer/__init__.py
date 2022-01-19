import requests
from logging import getLogger
from multiprocessing.pool import ThreadPool

from eltyer.configuration.config import Config
from eltyer.utils.version import get_version
from eltyer.models import OrderSide, OrderType, Order, Position, Portfolio, \
    OrderStatus
from eltyer.exceptions import ClientException

VERSION = (0, 2, 0, 'alpha', 0)

logger = getLogger(__name__)


class Client:
    config = Config()
    thread_count = 2
    _pool = None

    # Algorithm specific attributes
    algorithm_id = None
    environment = None

    def start(self):

        if not self.config.configured:
            raise ClientException("Client is not configured")

        algorithm_data = self._retrieve_algorithm()
        Client.algorithm_id = algorithm_data["algorithm_id"]
        Client.environment = algorithm_data["environment"]

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
            f"{self.config.HOST_ORDER_SERVICE}{self.config.ORDERS_ENDPOINT}",
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
            f"{self.config.HOST_ORDER_SERVICE}{self.config.ORDERS_ENDPOINT}",
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
            f"{self.config.HOST_ORDER_SERVICE}"
            f"{self.config.LIST_ORDERS_ENDPOINT.format(algorithm_id=self.algorithm_id)}",
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
            f"{self.config.HOST_ORDER_SERVICE}"
            f"{self.config.LIST_ORDERS_ENDPOINT.format(algorithm_id=self.algorithm_id)}",
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

        response = requests.get(
            f"{self.config.HOST_ORDER_SERVICE}"
            f"{self.config.POSITIONS_ENDPOINT.format(algorithm_id=self.algorithm_id)}",
            params={"itemized": True},
            headers={"x-api-key": self.config.API_KEY}
        )

        data = self._handle_response(response)

        if json:
            return data["items"]

        positions = []

        for position_data in data["items"]:
            positions.append(Position.from_dict(position_data))

        return positions

    def get_position(self, symbol: str, json=False):
        self.check_context()

        response = requests.get(
            f"{self.config.HOST_ORDER_SERVICE}"
            f"{self.config.POSITIONS_ENDPOINT.format(algorithm_id=self.algorithm_id)}",
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
            f"{self.config.HOST_ORDER_SERVICE}"
            f"{self.config.PORTFOLIO_ENDPOINT.format(algorithm_id=self.algorithm_id)}",
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

            raise ClientException(response.json()["error_message"])

        return response.json()

    def _retrieve_algorithm(self):
        response = requests.get(
            f"{self.config.HOST_ORDER_SERVICE}"
            f"{self.config.API_KEY_VERIFY_ENDPOINT}",
            headers={"x-api-key": self.config.API_KEY}
        )

        return self._handle_response(response)

    def check_context(self):

        if self.algorithm_id is None:
            raise ClientException("Client is not configured")


__all__ = [
    "Client",
    "get_version",
    "OrderType",
    "OrderStatus",
    "OrderSide",
    "ClientException"
]
