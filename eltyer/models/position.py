from eltyer.models.model import Model
from eltyer.models.order import Order


class Position(Model):

    def __init__(self, id, symbol, amount, percentage, orders):
        self.id = id
        self.symbol = symbol
        self.amount = amount
        self.percentage = percentage
        self.orders = []

        if orders is not None:
            for order_data in orders:
                self.orders.append(Order.from_dict(order_data))

    @staticmethod
    def from_dict(data):
        return Position(
            id=data.get("id", None),
            symbol=data.get("symbol", None),
            amount=data.get("amount", None),
            percentage=data.get("percentage", None),
            orders=data.get("orders", None)
        )

    def to_dict(self):
        return {
            "id": self.get_id(),
            "symbol": self.get_symbol(),
            "amount": self.get_amount(),
            "percentage": self.get_percentage(),
            "orders": self.get_orders(json=True),
            "target_symbol": self.get_symbol()
        }

    def __repr__(self):
        return self.repr(
            id=self.id,
            symbol=self.symbol,
            amount=self.amount,
            percentage=self.percentage,
            orders=self.orders
        )

    def get_id(self):
        return self.id

    def get_orders(self, json=False):

        if json:
            data = []

            for order in self.orders:
                data.append(order.to_dict())
                return data

        return self.orders

    def get_symbol(self):
        return self.symbol

    def get_percentage(self):
        return self.percentage

    def get_amount(self):
        return self.amount
