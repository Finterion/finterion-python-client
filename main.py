from eltyer import Client, OrderStatus

# Create a client and configure it with your algorithm api keys from ELTYER
client = Client()

# ****Configuration options****

# Configuration with dict
client.config.from_dict({"API_KEY": "91X8SUecOCDYXMvaLDNM63RyiIDFimyHXbeIP5ycUSMMeSt0Vc3lZULffc25bDmG"})

if __name__ == "__main__":
    # Start the ELTYER client
    client.start()

    # Get the api key context/environment
    print(client.get_environment())

    # Create a limit order
    limit_order = client.create_limit_order(
        target_symbol="btc", amount=1, price=10, side="BUY",
    )

    print(limit_order)