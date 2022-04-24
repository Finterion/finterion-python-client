from unittest import TestCase

from eltyer.models import Position


class Test(TestCase):

    def test_from_dict(self):
        position = Position.from_dict(
            {
                "id": 1,
                "amount": 10,
                "symbol": "USDT",
                "percentage": 10,
                "orders": []
            }
        )

        self.assertIsNotNone(position)
        self.assertIsNotNone(position.get_symbol())
        self.assertIsNotNone(position.get_orders())
        self.assertIsNotNone(position.get_id())
        self.assertIsNotNone(position.get_amount())
        self.assertIsNotNone(position.get_percentage())

    def test_with_amount_and_symbol(self):

        position = Position.from_dict(
            {
                "amount": 10,
                "symbol": "USDT",
            }
        )

        self.assertIsNotNone(position)
        self.assertIsNotNone(position.get_symbol())
        self.assertIsNotNone(position.get_orders())
        self.assertIsNone(position.get_id())
        self.assertIsNotNone(position.get_amount())
        self.assertIsNone(position.get_percentage())

    def test_from_dict_with_orders(self):
        position = Position.from_dict(
            {
                "id": 1,
                "amount": 10,
                "symbol": "USDT",
                "percentage": 10,
                "orders": [
                    {
                        "id": 1,
                        "target_symbol": "BTC",
                        "trading_symbol": "USDT",
                        "amount_target_symbol": 10,
                        "amount_trading_symbol": 100,
                        "initial_price": 10,
                        "side": "BUY",
                        "status": "SUCCESS",
                        "type": "LIMIT",
                        "order_reference": 2
                    },
                    {
                        "id": 2,
                        "target_symbol": "BTC",
                        "trading_symbol": "USDT",
                        "amount_target_symbol": 10,
                        "amount_trading_symbol": 100,
                        "initial_price": 10,
                        "side": "BUY",
                        "status": "SUCCESS",
                        "type": "LIMIT",
                        "order_reference": 2
                    }
                ]
            }
        )

        self.assertIsNotNone(position)
        self.assertIsNotNone(position.get_symbol())
        self.assertIsNotNone(position.get_orders())
        self.assertIsNotNone(position.get_id())
        self.assertIsNotNone(position.get_amount())
        self.assertIsNotNone(position.get_percentage())
        self.assertIsNotNone(position.get_orders())
        self.assertEqual(2, len(position.get_orders()))
