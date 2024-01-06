from django.db import models
from ..enums.booking_status import BookingStatus
from .base_model import BaseModel
from .customer import Customer
from .show import Show
from .show_seat import ShowSeat


class Booking(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    # one booking can have multiple show_seats
    # one show_seat can be part of multiple bookings
    show_seat = models.ManyToManyField(ShowSeat)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    booked_at = models.DateTimeField(auto_now_add=True)
    booking_status = models.CharField(
        max_length=100,
        choices=[
            (booking_status.value, booking_status.name)
            for booking_status in BookingStatus
        ],
    )
