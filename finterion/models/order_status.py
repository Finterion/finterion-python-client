from enum import Enum


class OrderStatus(Enum):
    SUCCESS = 'SUCCESS'
    PENDING = 'PENDING'
    TO_BE_SENT = "TO_BE_SENT"
    FAILED = "FAILED"
    CANCELED = "CANCELED"
    CLOSED = "CLOSED"

    @staticmethod
    def from_value(value):

        if isinstance(value, str):
            for order_type in OrderStatus:

                if value.upper() == order_type.value:
                    return order_type
        elif isinstance(value, OrderStatus):
            for status in OrderStatus:

                if value == status:
                    return status

        return None

    def equals(self, other):

        if other is None:
            return False

        if isinstance(other, Enum):
            return self.value == other.value

        else:
            return OrderStatus.from_string(other) == self

    def __str__(self):
        return str(self.value)
