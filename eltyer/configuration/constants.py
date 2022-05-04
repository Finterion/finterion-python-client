BASE_URL = "https://api.eltyer.com"

ELTYER_API_KEY = "ELTYER_API_KEY"
API_KEY = "API_KEY"
CLOUD_FUNCTION = "CLOUD_FUNCTION"

ORDER_SERVICE_URL = f"{BASE_URL}/order-service"
ORCHESTRATION_SERVICE_ULR = f"{BASE_URL}/orchestration-service"
ALGORITHM_SERVICE_URL = f"{BASE_URL}/algorithm-service"

ORDERS_ENDPOINT = ORDER_SERVICE_URL + "/v1/orders"
LIST_ORDERS_ENDPOINT = ORDER_SERVICE_URL + \
                       "/v1/algorithms/{algorithm_id}/orders"
API_KEY_VERIFY_ENDPOINT = ORDER_SERVICE_URL + "/v1/algorithms/api-keys/verify"
POSITIONS_ENDPOINT = ORDER_SERVICE_URL + \
                     "/v1/algorithms/{algorithm_id}/positions"
PORTFOLIO_ENDPOINT = ORDER_SERVICE_URL + \
                     "/v1/algorithms/{algorithm_id}/portfolio"
ORCHESTRATION_CREATION_ENDPOINT = ORCHESTRATION_SERVICE_ULR +\
                                  "/v1/subscriptions/algorithms/{algorithm_id}"
ORCHESTRATION_ONLINE_ENDPOINT = ORCHESTRATION_SERVICE_ULR +\
                                "/v1/subscriptions/algorithms/{algorithm_id}/"\
                                "{environment}/online"
SUBSCRIPTION_STATUS = ORCHESTRATION_SERVICE_ULR + \
                      "/v1/subscriptions/algorithms/{algorithm_id}/" \
                      "{environment}/status"
