from django.db import models
from ..enums.seat_type import SeatType
from .audi import Audi
from .base_model import BaseModel


class Seat(BaseModel):
    row_no = models.IntegerField()
    column_no = models.IntegerField()
    seat_type = models.CharField(
        max_length=100,
        choices=[(seat_type.value, seat_type.name) for seat_type in SeatType],
    )
    audi = models.ForeignKey(Audi, on_delete=models.CASCADE)
