from django.db import models

from euth.contrib import base_models


class Post(base_models.TimeStampedModel):

    heading = models.CharField(max_length=200)
    body = models.TextField()
