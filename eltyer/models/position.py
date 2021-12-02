from eltyer.models.model import Model


class Position(Model):

    def __init__(self, id, symbol, amount, percentage, orders):
        self.id = id
        self.symbol = symbol
        self.amount = amount
        self.percentage = percentage
        self.orders = orders

    @staticmethod
    def from_dict(data):
        return Position(
            id=data.get("id", None),
            symbol=data.get("symbol", None),
            amount=data.get("amount", None),
            percentage=data.get("percentage", None),
            orders=data.get("orders", None)
        )

    def __repr__(self):
        return self.repr(
            id=self.id,
            symbol=self.symbol,
            amount=self.amount,
            percentage=self.percentage,
            orders=self.orders
        )
