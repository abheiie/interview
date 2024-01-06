from django.db import models
from ..enums.feature import Feature
from ..enums.language import Language
from .base_model import BaseModel


class Movie(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    duration = models.IntegerField()
    rating = models.IntegerField()
    language = models.CharField(
        max_length=100,
        choices=[(language.value, language.name) for language in Language],
    )
    feature = models.CharField(
        max_length=100,
        choices=[(feature.value, feature.name) for feature in Feature],
    )
