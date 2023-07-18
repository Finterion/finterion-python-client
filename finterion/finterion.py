from finterion import services, ClientException, OrderSide


class Finterion:

    def __init__(self, api_key):
        self.api_key = api_key
        self.ping()
        self.algorithm = self.get_algorithm_model()

    def ping(self):
        return services.ping(self.api_key)

    def get_algorithm_model(self):
        return services.get_algorithm_model(self.api_key)

    def get_orders(self, status=None, target_symbol=None, symbol=None, order_type=None, order_side=None):
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

        orders = services.get_orders(self.api_key, query_params)
        return orders["items"]

    def get_order(self, order_id):
        return services.get_order(self.api_key, order_id)

    def create_order(self, target_symbol, order_side, order_type, amount, price):
        data = {
            "target_symbol": target_symbol,
            "side": order_side,
            "type": order_type,
            "amount": amount,
            "price": price
        }
        return services.create_order(self.api_key, data)

    def create_limit_order(self, target_symbol, order_side, amount, price):
        data = {
            "target_symbol": target_symbol,
            "side": order_side,
            "type": "LIMIT",
            "amount": amount,
            "price": price
        }
        return services.create_order(self.api_key, data)

    def create_market_order(self, target_symbol, order_side, amount):

        if OrderSide.BUY.equals(order_side):
            raise ClientException(
                "Market orders are not supported for BUY orders"
            )

        data = {
            "target_symbol": target_symbol,
            "side": order_side,
            "type": "MARKET",
            "amount": amount,
        }
        return services.create_order(self.api_key, data)

    def get_position(self, position_id):
        return services.get_position(self.api_key, position_id)

    def get_positions(self, symbol=None):
        query_params = {"itemized": "true"}

        if symbol is not None:
            query_params["symbol"] = symbol

        positions = services.get_positions(self.api_key, query_params)
        return positions["items"]

    def get_portfolio(self):
        return services.get_portfolio(self.api_key)
