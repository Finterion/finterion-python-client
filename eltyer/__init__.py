import requests
from logging import getLogger
from multiprocessing.pool import ThreadPool

from eltyer.configuration.config import Config
from eltyer.utils.version import get_version
from eltyer.models import OrderSide, OrderType, Order
from eltyer.exceptions import ClientException

VERSION = (0, 0, 1, 'alpha', 0)

logger = getLogger(__name__)


class Client:
    config = Config()
    thread_count = 2
    _pool = None

    def start(self):

        if not self.config.configured:
            raise ClientException("Client is not configured")

    def stop(self):
        if self._pool:
            self._pool.close()
            self._pool.join()
            self._pool = None

    @property
    def pool(self):
        if self._pool is None:
            self._pool = ThreadPool(self.thread_count)

        return self._pool

    def get_orders(self):
        pass

    def create_limit_order(
        self,
        symbol: str,
        price: float,
        amount: float,
        side: str = OrderSide.BUY.value
    ) -> Order:
        payload = {
            "target_symbol": symbol,
            "price": price,
            "amount": amount,
            "side": OrderSide.from_value(side).value,
            "type": OrderType.LIMIT.value,
        }

        response = requests.post(
            f"{self.config.HOST}{self.config.ORDERS_ENDPOINT}",
            json=payload,
            headers={"x-api-key": self.config.API_KEY}
        )

        data = self._handle_response(response)
        return Order.from_dict(data)

    def create_market_order(
        self,
        symbol: str,
        price: float,
        amount: float,
        side: str = OrderSide.SELL.value
    ) -> Order:
        payload = {
            "target_symbol": symbol,
            "price": price,
            "amount": amount,
            "side": OrderSide.from_value(side).value,
            "type": OrderType.MARKET.value,
        }

        response = requests.post(
            f"{self.config.HOST}{self.config.ORDERS_ENDPOINT}",
            json=payload,
            headers={"x-api-key": self.config.API_KEY}
        )

        data = self._handle_response(response)
        return Order.from_dict(data)

    def get_pending_orders(self):
        pass

    def get_positions(self):
        pass

    def get_portfolio(self):
        pass

    def _handle_response(self, response):

        if response.status_code >= 400:

            if response.status_code == 500:
                raise ClientException("Something went wrong at ELTYER")

            raise ClientException(response.json()["error_message"])

        return response.json()


__all__ = ["Client", "get_version"]
