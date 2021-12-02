from eltyer.models.order_status import OrderStatus
from eltyer.models.order_side import OrderSide
from eltyer.models.order_type import OrderType
from eltyer.models.model import Model


class Order(Model):

    def __init__(
        self,
        id,
        side,
        type,
        target_symbol,
        trading_symbol,
        status,
        initial_price=None,
        amount_target_symbol=None,
        amount_trading_symbol=None,
    ):
        self.id = id,
        self.side = OrderSide.from_value(side)
        self.type = OrderType.from_value(type)
        self.target_symbol = target_symbol
        self.trading_symbol = trading_symbol
        self.status = OrderStatus.from_value(status)
        self.initial_price = initial_price
        self.amount_trading_symbol = amount_trading_symbol
        self.amount_target_symbol = amount_target_symbol

    @staticmethod
    def from_dict(data):
        return Order(
            id=data.get("id", None),
            side=data.get("side", None),
            type=data.get("type", None),
            target_symbol=data.get("target_symbol", None),
            trading_symbol=data.get("trading_symbol", None),
            status=data.get("status", None),
            initial_price=data.get("initial_price", None),
            amount_target_symbol=data.get("amount_target_symbol", None),
            amount_trading_symbol=data.get("amount_trading_symbol", None),
        )

    def __repr__(self):
        return self.repr(
            id=self.id,
            side=self.side.value,
            type=self.type.value,
            target_symbol=self.target_symbol,
            trading_symbol=self.trading_symbol,
            status=self.status.value,
            initial_price=self.initial_price,
            amount_target_symbol=self.amount_target_symbol,
            amount_trading_symbol=self.amount_trading_symbol,
        )
