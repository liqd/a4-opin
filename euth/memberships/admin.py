from django.contrib import admin

from . import models

admin.site.register(models.Request)
admin.site.register(models.Invite)
