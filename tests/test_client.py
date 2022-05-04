from unittest import TestCase

from eltyer import Client
from eltyer.models import Order


class ConfigTest(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.client.config.API_KEY = \
            "cbnu5EUlzF3empnASvYvQzTwSsiQTiAXiKIvDvT7ZLM3wXhYhaG2vTAlKFL4tNYn"

    def tearDown(self) -> None:
        self.client = Client()
        self.client.config.API_KEY = None

    def test_start(self):
        self.client.start()
        self.assertIsNotNone(self.client.status)

    def test_get_portfolio(self):
        self.client.start()
        self.assertIsNotNone(self.client.get_portfolio())

    def test_create_limit_order(self):
        self.client.start()
        order = self.client.create_limit_order(
            target_symbol="BTC", amount=10, price=10
        )
        self.assertIsNotNone(order)
        self.assertTrue(isinstance(order, Order))

    def test_list_orders(self):
        self.client.start()
        orders = self.client.get_orders()
        self.assertEqual(orders, [])

    def test_list_positions(self):
        self.client.start()
        positions = self.client.get_positions()
        self.assertEqual(len(positions), 1)
