from eltyer.models.model import Model


class Portfolio(Model):

    def __init__(
        self,
        id,
        algorithm_id,
        trading_symbol,
        delta,
        allocated,
        allocated_percentage,
        unallocated,
        unallocated_percentage,
        broker,
        realized,
        created_at,
        updated_at,
        orders,
        positions,
        **kwargs
    ):
        self.id = id
        self.algorithm_id = algorithm_id
        self.delta = delta
        self.allocated = allocated
        self.allocated_percentage = allocated_percentage
        self.trading_symbol = trading_symbol
        self.unallocated = unallocated
        self.unallocated_percentage = unallocated_percentage
        self.realized = realized
        self.orders = orders
        self.positions = positions
        self.broker = broker
        self.created_at = created_at
        self.updated_at = updated_at
        super(Portfolio, self).__init__(**kwargs)

    @staticmethod
    def from_dict(data):
        return Portfolio(
            id=data.get("id", None),
            algorithm_id=data.get("algorith_id", None),
            delta=data.get("delta", None),
            allocated=data.get("allocated", None),
            allocated_percentage=data.get("allocated_percentage", None),
            trading_symbol=data.get("trading_symbol", None),
            unallocated=data.get("unallocated", None),
            unallocated_percentage=data.get("unallocated_percentage", None),
            realized=data.get("realized", None),
            orders=data.get("orders", None),
            positions=data.get("positions", None),
            broker=data.get("broker", None),
            created_at=data.get("created_at", None),
            updated_at=data.get("updated_at", None),
        )

    def __repr__(self):
        return self.repr(
            id=self.id,
            algorithm_id=self.algorithm_id,
            delta=self.delta,
            allocated=self.allocated,
            allocated_percentage=self.allocated_percentage,
            trading_symbol=self.trading_symbol,
            unallocated=self.unallocated,
            unallocated_percentage=self.unallocated_percentage,
            realized=self.realized,
            orders=self.orders,
            positions=self.positions,
            broker=self.broker,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
