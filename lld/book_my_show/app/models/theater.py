from django.db import models
from .base_model import BaseModel
from .city import City


class Theater(BaseModel):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
