from django.db import models
from .base_model import BaseModel
from .user import User


class Customer(BaseModel):
    full_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=254, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
