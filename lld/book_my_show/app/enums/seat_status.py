from enum import Enum


class SeatStatus(Enum):
    BOOKED = "BOOKED"
    AVAILABLE = "AVAILABLE"
    LOCKED = "LOCKED"
