from unittest import TestCase

from eltyer.models import Order


class Test(TestCase):

    def test_from_dict(self):
        order = Order.from_dict(
            {
                "id": 1,
                "target_symbol": "BTC",
                "trading_symbol": "USDT",
                "amount_target_symbol": 10,
                "amount_trading_symbol":  100,
                "initial_price": 10,
                "side": "BUY",
                "status": "SUCCESS",
                "type": "LIMIT",
                "order_reference": 2
            }
        )

        self.assertIsNotNone(order)
        self.assertIsNotNone(order.get_order_reference())
        self.assertIsNotNone(order.get_id())
        self.assertIsNotNone(order.get_type())
        self.assertIsNotNone(order.get_side())
        self.assertIsNotNone(order.get_initial_price())
        self.assertIsNotNone(order.get_amount_target_symbol())
        self.assertIsNotNone(order.get_amount_trading_symbol())
        self.assertIsNotNone(order.get_target_symbol())
        self.assertIsNotNone(order.get_trading_symbol())
