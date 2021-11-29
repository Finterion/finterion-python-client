[![Tests](https://github.com/ELTYER/eltyer-python-client/actions/workflows/test.yml/badge.svg)](https://github.com/ELTYER/eltyer-python-client/actions/workflows/test.yml)

# Official ELTYER Python Client

> :warning: **Documentation outdated**: We are working hard on releasing v1.0.0. After 
> this release we will update the documentation at the website.

The ELTYER python client is a python library that can be used in your investing algorithm.
With this client your can connect your algorithm to the ELTYER.

## Installation
You can install the client directly using pip:

```sh
pip install eltyer_client
```

## Usage
Example usage
```python
from eltyer import Client

# Create an client and configure it
client = Client()

# ****Configuration options****

# Configuration with dict 
client.config.from_dict({"api_key": "<YOUR_API_KEY>"})

# Configuration with attribute setter
client.config.api_key = "<YOUR_API_KEY>"

# Configuration with environment variable 'ELTYER_API_KEY'
client.config.from_env()

# ****Configuration options****

# ****Available Operations****

# Start the ELTYER client
client.start()

# Create an limit order
limit_order = client.create_order()

# List all orders
orders = client.get_orders()

# List all pending orders
pending_orders = client.get_pending_orders()

# Get the order status
status = client.get_order_status(limit_order.id)

# Retrieve all your positions
positions = client.get_positions()

# Retrieve a specific position
position = client.get_position("BTC")

# Retrieve the portfolio of your algorithm
portfolio = client.get_portfolio()

# Stop the client
client.stop()

```




