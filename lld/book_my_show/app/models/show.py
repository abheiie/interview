from django.db import models
from .audi import Audi
from .base_model import BaseModel
from .movie import Movie


class Show(BaseModel):
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    audi = models.ForeignKey(Audi, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
