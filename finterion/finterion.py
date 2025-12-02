import logging
from finterion import services, ClientException, OrderSide


logger = logging.getLogger("finterion")


class Finterion:
    """
    Finterion REST API client implementation.
    Provides methods to interact with the Finterion API.

    Attributes:
        api_key (str): API key for authentication.
        base_url (str): Base URL for the Finterion API.
        algorithm (dict): Algorithm model retrieved from the API.
    """

    def __init__(self, api_key, base_url=None):
        """
        Initializes the Finterion client with the provided
        API key and base URL. If no base URL is provided,
        a default URL is used. The API key is stripped of
        any surrounding quotes before being stored.

        Args:
            api_key (str): API key for authentication.
            base_url (str, optional): Base URL for the Finterion API.
                Defaults to None.

        Returns:
            None
        """
        self.api_key = api_key.strip('\'"')
        self.base_url = base_url

        if self.base_url is None:
            self.base_url = "https://api.finterion.com/algs"
        else:
            logger.info(
                f"Setup Finterion client with base url {self.base_url}"
            )

        self.algorithm = self.get_algorithm_model()

    def ping(self):
        """
        Pings the Finterion API with the provided algorithm API key.

        Returns:
            dict: Response from the ping request.
        """
        return services.ping(self.api_key, base_url=self.base_url)

    def get_algorithm_model(self):
        """
        Retrieves the algorithm model from the Finterion API.

        Returns:
            dict: Algorithm model data.
        """
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
        """
        Retrieves a list of orders from the Finterion API
        based on the provided filters.

        Args:
            status (str, optional): Filter orders by status. Defaults to None.
            target_symbol (str, optional): Filter orders by target symbol.
                Defaults to None.
            symbol (str, optional): Filter orders by symbol. Defaults to None.
            order_type (str, optional): Filter orders by type. Defaults
                to None.
            order_side (str, optional): Filter orders by side. Defaults
                to None.
            query_params (dict, optional): Additional query parameters.
                Defaults to None.

        Returns:
            list: List of orders matching the filters.
        """

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
        """
        Retrieves a specific order from the Finterion API
        based on the provided order ID.

        Args:
            order_id (str): ID of the order to retrieve.
            query_params (dict, optional): Additional query parameters.
                Defaults to None.

        Returns:
            dict: Order data.
        """
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
        """
        Creates a new order on the Finterion platform.

        Args:
            target_symbol (str): The target symbol for the order.
            order_side (str): The side of the order (buy/sell).
            order_type (str): The type of the order (limit/market).
            amount (str): The amount for the order.
            price (str): The price for the order.

        Returns:
            dict: Response from the create order request.
        """
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
        """
        Creates a limit order on the Finterion platform.

        Args:
            target_symbol (str): The target symbol for the order.
            order_side (str): The side of the order (buy/sell).
            amount (str): The amount for the order.
            price (str): The price for the order.

        Returns:
            dict: Response from the create limit order request.
        """
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
        """
        Creates a market order on the Finterion platform.

        Args:
            target_symbol (str): The target symbol for the order.
            order_side (str): The side of the order (buy/sell).
            amount (str): The amount for the order.

        Returns:
            dict: Response from the create market order request.
        """
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
        """
        Retrieves a specific position from the Finterion API
        based on the provided position ID.

        Args:
            position_id (str): ID of the position to retrieve.
            query_params (dict, optional): Additional query parameters.
                Defaults to None.

        Returns:
            dict: Position data.
        """
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
        """
        Retrieves a list of positions from the Finterion API based on
        the provided filters.

        Args:
            symbol (str, optional): Filter positions by symbol. Defaults
                to None.
            query_params (dict, optional): Additional query parameters.
                Defaults to None.

        Returns:
            list: List of positions matching the filters.
        """
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
        """
        Retrieves the portfolio from the Finterion API.

        Args:
            query_params (dict, optional): Additional query parameters.
                Defaults to None.

        Returns:
            dict: Portfolio data.
        """
        if query_params is None:
            query_params = {}

        response = services.get_portfolio(
            api_key=self.api_key,
            query_params=query_params,
            base_url=self.base_url
        )
        logger.debug(f"get_portfolio response {response}")
        return response

    def get_supported_symbols(self):
        """
        Retrieves the list of supported symbols from the Finterion API
        for the given algorithm profile.

        Returns:
            dict: List of supported symbols.
        """
        response = services.get_supported_symbols(
            api_key=self.api_key,
            base_url=self.base_url
        )
        logger.debug(f"get_supported_symbols response {response}")
        return response
