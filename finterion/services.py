import json

import requests
import logging
from finterion.configuration import constants
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
        raise ClientException(response.json()["message"])
    else:
        raise ClientException("Error connecting to finterion platform")


def ping(api_key, url=constants.PING_ENDPOINT):
    response = requests.get(url, headers={"XApiKey": api_key})
    return handle_response(response)


def get_algorithm_model(api_key, url=constants.ALGORITHM_ENDPOINT):
    response = requests.get(url, headers={"XApiKey": api_key})
    return handle_response(response)


def get_orders(api_key, query_params, url=constants.LIST_ORDERS_ENDPOINT):
    response = requests.get(
        url, headers={"XApiKey": api_key}, params=query_params
    )
    return handle_response(response)


def get_order(api_key, query_params, url=constants.RETRIEVE_ORDER_ENDPOINT):
    response = requests.get(
        url, headers={"XApiKey": api_key}, params=query_params
    )
    return handle_response(response)


def create_order(api_key, data, url=constants.CREATE_ORDER_ENDPOINT):
    response = requests.post(
        url, headers={"XApiKey": api_key}, json=json.dumps(data)
    )
    return handle_response(response)


def get_positions(api_key, query_params, url=constants.LIST_POSITIONS):
    response = requests.get(
        url, headers={"XApiKey": api_key}, params=query_params
    )
    return handle_response(response)


def get_position(api_key, position_id, url=constants.RETRIEVE_POSITION):
    response = requests.get(
        url.format(position_id=position_id), headers={"XApiKey": api_key}
    )
    return handle_response(response)


def get_portfolio(api_key, url=constants.PORTFOLIO_ENDPOINT):
    response = requests.get(url, headers={"XApiKey": api_key})
    return handle_response(response)
