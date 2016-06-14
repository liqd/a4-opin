from django.contrib import admin

from . import models

admin.site.register(models.Process)
admin.site.register(models.ParticipationModule)
admin.site.register(models.Phase)
