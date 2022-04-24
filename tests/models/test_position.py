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
        self.assertIsNone(position.get_orders())
        self.assertIsNone(position.get_id())
        self.assertIsNotNone(position.get_amount())
        self.assertIsNone(position.get_percentage())
