[![Tests](https://github.com/finterion/finterion-python-client/actions/workflows/test.yml/badge.svg)](https://github.com/finterion/finterion-python-client/actions/workflows/test.yml)
[![Build](https://github.com/finterion/finterion-python-client/actions/workflows/build.yml/badge.svg)](https://github.com/finterion/finterion-python-client/actions/workflows/build.yml)
# Official Finterion Python Client

<a href="https://www.finterion.com/" target="_blank">
    <picture style="height: 30px;">
    <source media="(prefers-color-scheme: dark)" srcset="static/sponsors/finterion-dark.png">
    <source media="(prefers-color-scheme: light)" srcset="static/sponsors/finterion-light.png">
    <img src="static/sponsors/finterion-light.png" alt="Finterion Logo" width="200px" height="50px">
    </picture>
</a>


The Finterion python client is a python library that can be used by your 
trading bots/quantitative trading strategies that are registered at the [Finterion platform](https://finterion.com). 
It provides a simple and easy-to-use interface for interacting with the Finterion API.

## Installation
You can install the client directly using pip:

```sh
pip install finterion
```

## Usage
Example usage
```python
from finterion import Finterion, OrderStatus, OrderSide, OrderType

# Create a client and configure it with your algorithm api keys from Finterion
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
positions = client.get_positions(symbol="btc")
position = client.get_position(positions[0].id)

# Get orders
orders = client.get_orders()
orders = client.get_orders(
    target_symbol="btc", 
    status=OrderStatus.PENDING,
    order_type=OrderType.LIMIT,
    order_side=OrderSide.BUY
)
order = client.get_order(orders[0].id)

# Get the portfolio
portfolio = client.get_portfolio()
```

## Documentation
You can find the official documentation at our [documentation website](https://docs.finterion.com/python-client/introduction)
