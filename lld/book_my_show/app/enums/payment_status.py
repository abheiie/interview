from enum import Enum


class PaymentStatus(Enum):
    DONE = "DONE"
    PENDING = "PENDING"
    FAILED = "FAILED"
