def get_retrieve_order_url(base_url, order_id):
    return f"{base_url}/orders/{order_id}"


def get_list_orders_url(base_url):
    return f"{base_url}/orders"


def create_order_url(base_url):
    return f"{base_url}/orders"


def get_ping_url(base_url):
    return f"{base_url}/status/ping"


def get_algorithm_url(base_url):
    return base_url


def get_list_positions_url(base_url):
    return f"{base_url}/positions"


def get_retrieve_position_url(base_url, position_id):
    return f"{base_url}/positions/{position_id}"


def get_retrieve_portfolio_url(base_url):
    return f"{base_url}/portfolio"


def get_supported_symbols_url(base_url):
    return f"{base_url}/symbols"
