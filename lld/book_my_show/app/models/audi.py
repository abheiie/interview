from django.db import models

from .base_model import BaseModel
from .theater import Theater


class Audi(BaseModel):
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
