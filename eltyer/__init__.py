from multiprocessing.pool import ThreadPool

from eltyer.configuration.config import Config
from eltyer.utils.version import get_version

VERSION = (0, 0, 1, 'alpha', 0)


class Client:
    config = Config()
    thread_count = 2
    _pool = None

    def start(self):
        pass

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
    ):
        pass

    def create_market_order(self):
        pass

    def create_order(self):
        pass

    def get_pending_orders(self):
        pass

    def get_positions(self):
        pass

    def get_portfolio(self):
        pass


__all__ = ["Client", "get_version"]
