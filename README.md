[![Tests](https://github.com/ELTYER/eltyer-python-client/actions/workflows/test.yml/badge.svg)](https://github.com/ELTYER/eltyer-python-client/actions/workflows/test.yml)
[![Build](https://github.com/ELTYER/eltyer-python-client/actions/workflows/build.yml/badge.svg)](https://github.com/ELTYER/eltyer-python-client/actions/workflows/build.yml)
# Official ELTYER Python Client

The ELTYER python client is a python library that can be used by your 
investing algorithm. With this client your can connect your algorithm to 
the ELTYER platform.

## Installation
You can install the client directly using pip:

```sh
pip install finterion
```

## Usage
Example usage
```python
from finterion import Finterion, OrderStatus

# Create a client and configure it with your algorithm api keys from ELTYER
client = Finterion(api_key="<YOUR_API_KEY>")

# ****Available Operations****
# Get algorithm model
model = client.get_algorithm_model()

# Create a limit order
limit_order = client.create_limit_order(
    target_symbol="btc", amount=1, price=5, order_side="BUY",
)

# Create a market order (only sell market orders are supported)
market_order = client.create_market_order(
    target_symbol="btc", amount=1, order_side="SELL"
)

# Get positions
positions = client.get_positions()
position = client.get_position("btc")

# Get orders
orders = client.get_orders()
orders = client.get_orders(
    target_symbol="btc", status=OrderStatus.PENDING.value
)

# Get the portfolio
portfolio = client.get_portfolio()
```

## Documentation
You can find the official documentation at our [documentation website](https://docs.eltyer.com/python-client/introduction)



