from .base_model import BaseModel
from django.db import models


class City(BaseModel):
    name = models.CharField(max_length=255)
    # list of theater
