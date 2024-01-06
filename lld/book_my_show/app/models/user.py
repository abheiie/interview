from django.db import models
from .base_model import BaseModel


class User(BaseModel):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
