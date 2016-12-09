from django.db import models

from adhocracy4.models import base


class Post(base.TimeStampedModel):

    heading = models.CharField(max_length=200)
    body = models.TextField()
