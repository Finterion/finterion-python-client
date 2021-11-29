from eltyer.models.order_status import OrderStatus
from eltyer.models.order_side import OrderSide
from eltyer.models.order_type import OrderType
from eltyer.models.model import Model


class Order(Model):

    def __init__(
        self,
        id,
        order_side,
        order_type,
        target_symbol,
        trading_symbol,
        status,
        price=None,
        amount_target_symbol=None,
        amount_trading_symbol=None,
    ):
        self.id = id,
        self.order_side = OrderSide.from_string(order_side).value
        self.order_type = OrderType.from_string(order_type).value
        self.target_symbol = target_symbol
        self.trading_symbol = trading_symbol
        self.status = OrderStatus.from_string(status).value
        self.initial_price = price
        self.amount_trading_symbol = amount_trading_symbol
        self.amount_target_symbol = amount_target_symbol

    @staticmethod
    def from_dict(data):
        pass
