import uuid
from django.db import models


class Registration(models.Model):
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    username = models.TextField(max_length=255)
    email = models.EmailField()
    password = models.TextField(max_length=128)
    nexts = models.URLField(blank=True, null=True)
