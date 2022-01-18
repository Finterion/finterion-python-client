from enum import Enum


class OrderSide(Enum):
    SELL = 'SELL'
    BUY = 'BUY'

    @staticmethod
    def from_value(value):

        if isinstance(value, str):
            for order_side in OrderSide:

                if value.upper() == order_side.value:
                    return order_side
        elif isinstance(value, OrderSide):
            for order_side in OrderSide:

                if value == order_side:
                    return order_side

        raise ValueError("Could not convert value to OrderSide")

    def equals(self, other):

        if isinstance(other, Enum):
            return self.value == other.value

        else:
            return OrderSide.from_string(other) == self

    def __str__(self):
        return str(self.value)
