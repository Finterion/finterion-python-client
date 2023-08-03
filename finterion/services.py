import json
import logging

import requests

from finterion.configuration.urls import get_retrieve_order_url, \
    get_ping_url, get_algorithm_url, get_retrieve_portfolio_url, \
    get_retrieve_position_url, get_list_positions_url, get_list_orders_url, \
    create_order_url
from finterion.exceptions import ClientException

logger = logging.getLogger(__name__)


def handle_response(response):

    if response.status_code == 200 \
            or response.status_code == 201 \
            or response.status_code == 204:
        return response.json()
    if response.status_code == 401:
        raise ClientException("Unauthorized, check your API key")
    elif response.status_code == 400:
        data = response.json()
        logger.error(data)

        if "message" in data:
            raise ClientException(data["message"])

        if "error" in data:
            raise ClientException(data["error"])

        raise ClientException("Something went wrong")
    else:
        raise ClientException("Error connecting to finterion platform")


def ping(api_key, base_url):
    url = get_ping_url(base_url)
    response = requests.get(url, headers={"XApiKey": api_key})
    return handle_response(response)


def get_algorithm_model(api_key, base_url):
    url = get_algorithm_url(base_url)
    response = requests.get(url, headers={"XApiKey": api_key})
    return handle_response(response)


def get_orders(api_key, query_params, base_url):
    url = get_list_orders_url(base_url)
    response = requests.get(
        url, headers={"XApiKey": api_key}, params=query_params
    )
    return handle_response(response)


def get_order(api_key, order_id, base_url):
    url = get_retrieve_order_url(base_url, order_id)
    response = requests.get(url, headers={"XApiKey": api_key})
    return handle_response(response)


def create_order(api_key, data, base_url):
    url = create_order_url(base_url)
    headers = {"XApiKey": api_key, "Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return handle_response(response)


def get_positions(api_key, query_params, base_url):
    url = get_list_positions_url(base_url)
    response = requests.get(
        url, headers={"XApiKey": api_key}, params=query_params
    )
    return handle_response(response)


def get_position(api_key, position_id, base_url):
    url = get_retrieve_position_url(base_url, position_id)
    response = requests.get(url, headers={"XApiKey": api_key})
    return handle_response(response)


def get_portfolio(api_key, base_url):
    url = get_retrieve_portfolio_url(base_url)
    response = requests.get(url, headers={"XApiKey": api_key})
    return handle_response(response)
