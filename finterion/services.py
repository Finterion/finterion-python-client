import json
import logging

import requests

from finterion.configuration.urls import get_retrieve_order_url, \
    get_ping_url, get_algorithm_url, get_retrieve_portfolio_url, \
    get_retrieve_position_url, get_list_positions_url, get_list_orders_url, \
    create_order_url, get_supported_symbols_url
from finterion.exceptions import ClientException

logger = logging.getLogger("finterion")


def handle_response(response) -> dict:
    """
    Generic method to handle responses from the finterion platform.

    Args:
        response: Response object from requests library.

    Returns:
        dict: Parsed JSON response.
    """
    if response.status_code == 200 \
            or response.status_code == 201 \
            or response.status_code == 204:
        return response.json()
    if response.status_code == 401:
        raise ClientException("Unauthorized, check your API key")
    elif response.status_code == 400:
        logger.error("Service call failed")
        data = response.json()

        if isinstance(data, str):
            data = json.loads(data)

        if "message" in data:
            raise ClientException(data["message"])

        if "error" in data:
            raise ClientException(data["error"])

        raise ClientException("Something went wrong")
    else:
        raise ClientException("Error connecting to finterion platform")


def ping(api_key, base_url):
    """
    Pings the finterion platform to check connectivity.

    Args:
        api_key (str): API key for authentication.
        base_url (str): Base URL of the finterion platform.

    Returns:
        dict: Response from the ping request.
    """
    logger.debug("Pinging finterion platform")
    url = get_ping_url(base_url)
    response = requests.get(url, headers={"XApiKey": api_key})
    return handle_response(response)


def get_algorithm_model(api_key, base_url):
    """
    Retrieves the algorithm model from the finterion platform.

    Args:
        api_key (str): API key for authentication.
        base_url (str): Base URL of the finterion platform.

    Returns:
        dict: Algorithm model data.
    """
    logger.debug("Getting algorithm model")
    url = get_algorithm_url(base_url)
    response = requests.get(url, headers={"XApiKey": api_key})
    return handle_response(response)


def get_orders(api_key, query_params, base_url):
    """
    Retrieves a list of orders from the finterion platform.

    Args:
        api_key (str): API key for authentication.
        base_url (str): Base URL of the finterion platform.
        query_params (dict): Query parameters for filtering orders.

    Returns:
        dict: List of orders.
    """
    logger.debug("Getting orders")
    url = get_list_orders_url(base_url)
    response = requests.get(
        url, headers={"XApiKey": api_key}, params=query_params
    )
    return handle_response(response)


def get_order(api_key, order_id, base_url, query_params):
    """
    Retrieves a specific order from the finterion platform.

    Args:
        api_key (str): API key for authentication.
        order_id (str): ID of the order to retrieve.
        base_url (str): Base URL of the finterion platform.
        query_params (dict): Additional query parameters.

    Returns:
        dict: Order data.
    """
    logger.debug("Getting order")
    url = get_retrieve_order_url(base_url, order_id)
    response = requests.get(
        url,
        headers={"XApiKey": api_key},
        params=query_params
    )
    return handle_response(response)


def create_order(api_key, data, base_url):
    """
    Creates a new order on the finterion platform.

    Args:
        api_key (str): API key for authentication.
        data (dict): Order data to be sent in the request body.
        base_url (str): Base URL of the finterion platform.

    Returns:
        dict: Created order data.
    """
    logger.debug("Creating order")
    url = create_order_url(base_url)
    headers = {"XApiKey": api_key, "Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return handle_response(response)


def get_positions(api_key, query_params, base_url):
    """
    Retrieves a list of positions from the finterion platform.

    Args:
        api_key (str): API key for authentication.
        base_url (str): Base URL of the finterion platform.
        query_params (dict): Query parameters for filtering positions.

    Returns:
        dict: List of positions.
    """
    logger.debug("Getting positions")
    url = get_list_positions_url(base_url)
    response = requests.get(
        url, headers={"XApiKey": api_key}, params=query_params
    )
    return handle_response(response)


def get_position(api_key, position_id, base_url, query_params):
    """
    Retrieves a specific position from the finterion platform.

    Args:
        api_key (str): API key for authentication.
        position_id (str): ID of the position to retrieve.
        base_url (str): Base URL of the finterion platform.
        query_params (dict): Additional query parameters.

    Returns:
        dict: Position data.
    """
    logger.debug("Getting position")
    url = get_retrieve_position_url(base_url, position_id)
    response = requests.get(
        url,
        headers={"XApiKey": api_key},
        params=query_params
    )
    return handle_response(response)


def get_portfolio(api_key, base_url, query_params):
    """
    Retrieves the portfolio from the finterion platform.

    Args:
        api_key (str): API key for authentication.
        base_url (str): Base URL of the finterion platform.
        query_params (dict): Additional query parameters.

    Returns:
        dict: Portfolio data.
    """
    logger.debug("Getting portfolio")
    url = get_retrieve_portfolio_url(base_url)
    response = requests.get(
        url, headers={"XApiKey": api_key}, params=query_params
    )
    return handle_response(response)


def get_supported_symbols(api_key, base_url):
    """
    Retrieves the list of supported symbols from the finterion platform.

    Args:
        api_key (str): API key for authentication.
        base_url (str): Base URL of the finterion platform.

    Returns:
        dict: Supported symbols data.
    """
    logger.debug("Getting supported symbols")
    url = get_supported_symbols_url(base_url)
    response = requests.get(url, headers={"XApiKey": api_key})
    return handle_response(response)
