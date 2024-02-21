import logging
from finterion import services, ClientException, OrderSide


logger = logging.getLogger("finterion")


class Finterion:

    def __init__(self, api_key, base_url=None):
        self.api_key = api_key
        self.base_url = base_url

        if self.base_url is None:
            self.base_url = "https://api.finterion.com/algs"
        else:
            logger.info(
                f"Setup Finterion client with base url {self.base_url}"
            )

        self.algorithm = self.get_algorithm_model()

    def ping(self):
        return services.ping(self.api_key, base_url=self.base_url)

    def get_algorithm_model(self):
        response = services.get_algorithm_model(
            self.api_key, base_url=self.base_url
        )
        logger.debug(f"get_algorithm_model response {response}")
        return response

    def get_orders(
        self,
        status=None,
        target_symbol=None,
        symbol=None,
        order_type=None,
        order_side=None,
        query_params: dict = None
    ):

        if query_params is None:
            query_params = {}

        query_params["itemized"] = "true"
        query_params["environment"] = self.algorithm["environment"]

        if status is not None:
            query_params["status"] = status

        if target_symbol is not None:
            query_params["TargetSymbol"] = target_symbol

        if symbol is not None:
            query_params["symbol"] = symbol

        if order_type is not None:
            query_params["type"] = order_type

        if order_side is not None:
            query_params["side"] = order_side

        orders = services.get_orders(
            api_key=self.api_key,
            query_params=query_params,
            base_url=self.base_url
        )
        logger.debug(f"get_orders response {orders}")
        return orders["items"]

    def get_order(self, order_id, query_params: dict = None):

        if query_params is None:
            query_params = {}

        query_params["environment"] = self.algorithm["environment"]

        response = services.get_order(
            api_key=self.api_key,
            order_id=order_id,
            base_url=self.base_url,
            query_params=query_params
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
            api_key=self.api_key,
            base_url=self.base_url,
            data=data
        )
        logger.debug(f"create_order response {response}")
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
        logger.debug(f"create_limit_order response {response}")
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
        logger.debug(f"create_market_order response {response}")
        return response

    def get_position(self, position_id, query_params: dict = None):

        if query_params is None:
            query_params = {}

        query_params["environment"] = self.algorithm["environment"]

        response = services.get_position(
            api_key=self.api_key,
            position_id=position_id,
            base_url=self.base_url,
            query_params=query_params
        )
        logger.debug(f"get_position response {response}")
        return response

    def get_positions(self, symbol=None, query_params: dict = None):

        if query_params is None:
            query_params = {}

        query_params["itemized"] = "true"
        query_params["environment"] = self.algorithm["environment"]

        if symbol is not None:
            query_params["symbol"] = symbol

        positions = services.get_positions(
            self.api_key, query_params, base_url=self.base_url
        )
        logger.debug(f"get_positions response {positions}")
        return positions["items"]

    def get_portfolio(self, query_params: dict = None):
        if query_params is None:
            query_params = {}

        response = services.get_portfolio(
            api_key=self.api_key,
            query_params=query_params,
            base_url=self.base_url
        )
        logger.debug(f"get_portfolio response {response}")
        return response
