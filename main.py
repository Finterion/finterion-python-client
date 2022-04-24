from eltyer import Client

if __name__ == "__main__":
    client = Client()
    client.config.API_KEY = "cbnu5EUlzF3empnASvYvQzTwSsiQTiAXiKIvDvT7ZLM3wXhYhaG2vTAlKFL4tNYn"
    client.start()
    print(client.get_portfolio())
    print(client.get_positions(json=True))
