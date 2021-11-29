from eltyer.models.model import Model


class Position(Model):

    def __init__(self, id, symbol, amount, cost, orders):
        self.id = id
        self.symbol = symbol
        self.amount = amount
        self.cost = cost
        self.orders = orders

    @staticmethod
    def from_dict(data):
        pass
