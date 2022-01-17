[![Tests](https://github.com/ELTYER/eltyer-python-client/actions/workflows/test.yml/badge.svg)](https://github.com/ELTYER/eltyer-python-client/actions/workflows/test.yml)
[![Build](https://github.com/ELTYER/eltyer-python-client/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/ELTYER/eltyer-python-client/actions/workflows/build.yml)

# Official ELTYER Python Client

The ELTYER python client is a python library that can be used by your 
investing algorithm. With this client your can connect your algorithm to 
the ELTYER platform.

## Installation
You can install the client directly using pip:

```sh
pip install eltyer
```

## Usage
Example usage
```python
from eltyer import Client, OrderStatus

# Create a client and configure it with your algorithm api keys from ELTYER
client = Client()

# ****Configuration options****

# Configuration with dict
client.config.from_dict({"API_KEY": "<YOUR_API_KEY>"})

# Configuration with attribute setter
client.config.API_KEY = "<YOUR_API_KEY>"

# Configuration with environment variable 'ELTYER_API_KEY'
client.config.from_env()

# ****Configuration options****

# ****Available Operations****

# Start the ELTYER client
client.start()

# Get the api key context/environment
client.get_environment()

# Create a limit order
limit_order = client.create_limit_order(
    target_symbol="btc", amount=1, price=5, side="BUY",
)

# Create a market order (only sell market orders are supported)
market_order = client.create_market_order(target_symbol="btc", amount=1)

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

# Stop the client
client.stop()
```

## Documentation
You can find the official documentation at our [documentation website](https://docs.eltyer.com/python-client/introduction)



