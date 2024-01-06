from django.db import models
from ..enums.payment_method import PaymentMethod
from ..enums.payment_status import PaymentStatus
from .base_model import BaseModel


class Payment(BaseModel):
    reference = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits = 10, decimal_places=2)
    payment_method = models.CharField(
        max_length=255,
        choices=[
            (payment_method.value, payment_method.name)
            for payment_method in PaymentMethod
        ],
    )
    payment_status = models.CharField(
        max_length=255,
        choices=[
            (payment_status.value, payment_status.name)
            for payment_status in PaymentStatus
        ],
    )
