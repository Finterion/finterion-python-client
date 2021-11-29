from eltyer.models.model import Model


class Portfolio(Model):

    def __init__(
        self,
        id,
        trading_symbol,
        unallocated,
        realized,
        total_revenue,
        total_cost,
        broker,
        created_at,
        updated_at,
        **kwargs
    ):
        self.id = id
        self.trading_symbol = trading_symbol
        self.unallocated = unallocated
        self.realized = realized
        self.total_revenue = total_revenue
        self.total_cost = total_cost
        self.broker = broker
        self.created_at = created_at
        self.updated_at = updated_at
        super(Portfolio, self).__init__(**kwargs)

    @staticmethod
    def from_dict(data):
        pass
