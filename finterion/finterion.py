import logging
from finterion import services, ClientException, OrderSide


logger = logging.getLogger("finterion")


class Finterion:

    def __init__(self, api_key, base_url=None):
        self.api_key = api_key
        self.base_url = base_url

        if self.base_url is None:
            self.base_url = "https://api.finterion.com/algs"

        logger.info(f"Setup Finterion client with base url {self.base_url}")
        self.ping()
        self.algorithm = self.get_algorithm_model()

    def ping(self):
        return services.ping(self.api_key, base_url=self.base_url)

    def get_algorithm_model(self):
        response = services.get_algorithm_model(
            self.api_key, base_url=self.base_url
        )
        logger.info(f"get_algorithm_model response {response}")
        return response

    def get_orders(
        self,
        status=None,
        target_symbol=None,
        symbol=None,
        order_type=None,
        order_side=None
    ):
        query_params = {"itemized": "true"}

        if status is not None:
            query_params["status"] = status

        if target_symbol is not None:
            query_params["target_symbol"] = target_symbol

        if symbol is not None:
            query_params["symbol"] = symbol

        if order_type is not None:
            query_params["type"] = order_type

        if order_side is not None:
            query_params["side"] = order_side

        orders = services.get_orders(
            self.api_key, query_params, base_url=self.base_url
        )
        logger.info(f"get_orders response {orders}")
        return orders["items"]

    def get_order(self, order_id):
        response = services.get_order(
            self.api_key, order_id, base_url=self.base_url
        )
        logger.info(f"get_order response {response}")
        return response

    def create_order(
        self, target_symbol, order_side, order_type, amount, price
    ):
        data = {
            "target_symbol": target_symbol,
            "side": order_side,
            "type": order_type,
            "amount": amount,
            "price": price,
            "environment": self.algorithm["environment"],

        }
        response = services.create_order(
            self.api_key, base_url=self.base_url, data=data
        )
        logger.info(f"create_order response {response}")
        return response

    def create_limit_order(self, target_symbol, order_side, amount, price):
        data = {
            "target_symbol": target_symbol,
            "order_side": order_side,
            "order_type": "LIMIT",
            "amount": amount,
            "price": price,
            "environment": self.algorithm["environment"],
        }
        response = services.create_order(
            api_key=self.api_key, data=data, base_url=self.base_url
        )
        logger.info(f"create_limit_order response {response}")
        return response

    def create_market_order(self, target_symbol, order_side, amount):

        if OrderSide.BUY.equals(order_side):
            raise ClientException(
                "Market orders are not supported for BUY orders"
            )

        data = {
            "target_symbol": target_symbol,
            "order_side": order_side,
            "order_type": "MARKET",
            "amount": amount,
            "environment": self.algorithm["environment"],
        }
        response = services.create_order(
            api_key=self.api_key, data=data, base_url=self.base_url
        )
        logger.info(f"create_market_order response {response}")
        return response

    def get_position(self, position_id):
        response = services.get_position(
            self.api_key, position_id, base_url=self.base_url
        )
        logger.info(f"get_position response {response}")
        return response

    def get_positions(self, symbol=None):
        query_params = {"itemized": "true"}

        if symbol is not None:
            query_params["symbol"] = symbol

        positions = services.get_positions(
            self.api_key, query_params, base_url=self.base_url
        )
        logger.info(f"get_positions response {positions}")
        return positions["items"]

    def get_portfolio(self):
        response = services.get_portfolio(
            self.api_key, self.base_url
        )
        logger.info(f"get_portfolio response {response}")
        return response
