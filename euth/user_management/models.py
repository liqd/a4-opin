import uuid
from django.db import models

from django.contrib.auth.models import User

class Registration(models.Model):
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    username = models.TextField(max_length=255)
    email = models.EmailField()
    password = models.TextField(max_length=128)
    next_action = models.URLField(blank=True, null=True)


class Reset(models.Model):
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    next_action = models.URLField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
