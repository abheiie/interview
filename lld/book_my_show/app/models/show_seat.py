from django.db import models
from ..enums.seat_status import SeatStatus
from .base_model import BaseModel
from .seat import Seat
from .show import Show


class ShowSeat(BaseModel):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    seat_status = models.CharField(
        max_length=100,
        choices=[(seat_status.value, seat_status.name) for seat_status in SeatStatus],
    )
