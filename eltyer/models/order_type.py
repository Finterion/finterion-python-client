from enum import Enum


class OrderType(Enum):
    LIMIT = 'LIMIT'
    MARKET = 'MARKET'

    @staticmethod
    def from_value(value):

        if isinstance(value, str):
            for order_type in OrderType:

                if value.upper() == order_type.value:
                    return order_type
        elif isinstance(value, OrderType):
            for order_type in OrderType:

                if value == order_type:
                    return order_type

        raise ValueError("Could not convert value to OrderType")

    def equals(self, other):

        if isinstance(other, Enum):
            return self.value == other.value

        else:
            return OrderType.from_value(other) == self

    def __str__(self):
        return str(self.value)
