from eltyer.models.order_status import OrderStatus
from eltyer.models.order_side import OrderSide
from eltyer.models.order_type import OrderType
from eltyer.models.model import Model


class Order(Model):

    def __init__(
        self,
        id,
        order_reference,
        side,
        type,
        target_symbol,
        trading_symbol,
        status,
        initial_price=None,
        amount_target_symbol=None,
        amount_trading_symbol=None,
    ):
        self.id = id
        self.order_reference = order_reference
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
            id=data.get("id"),
            order_reference=data.get("order_reference"),
            side=data.get("side"),
            type=data.get("type"),
            target_symbol=data.get("target_symbol"),
            trading_symbol=data.get("trading_symbol"),
            status=data.get("status"),
            initial_price=data.get("initial_price"),
            amount_target_symbol=data.get("amount_target_symbol"),
            amount_trading_symbol=data.get("amount_trading_symbol"),
        )

    def to_dict(self):
        return {
            "id": self.id,
            "target_symbol": self.target_symbol(),
            "trading_symbol": self.get_trading_symbol(),
            "amount_target_symbol": self.get_amount_target_symbol(),
            "amount_trading_symbol":  self.get_amount_trading_symbol(),
            "initial_price": self.get_initial_price(),
            "side": self.get_side(),
            "status": self.get_status(),
            "type": self.get_type(),
            "order_reference": self.get_order_reference()
        }

    def __repr__(self):
        return self.repr(
            id=self.id,
            order_reference=self.order_reference,
            side=str(self.side),
            type=str(self.type),
            target_symbol=self.target_symbol,
            trading_symbol=self.trading_symbol,
            status=str(self.status),
            initial_price=self.initial_price,
            amount_target_symbol=self.amount_target_symbol,
            amount_trading_symbol=self.amount_trading_symbol,
        )

    def get_id(self):
        return self.id

    def get_order_reference(self):
        return self.order_reference

    def get_side(self):
        return self.side

    def get_type(self):
        return self.type

    def get_target_symbol(self):
        return self.target_symbol

    def get_trading_symbol(self):
        return self.trading_symbol

    def get_status(self):
        return self.status

    def get_initial_price(self):
        return self.initial_price

    def get_amount_target_symbol(self):
        return self.amount_target_symbol

    def get_amount_trading_symbol(self):
        return self.amount_trading_symbol