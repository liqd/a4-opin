from django.contrib import admin

from . import models

admin.site.register(models.User)
admin.site.register(models.Registration)
admin.site.register(models.Reset)
