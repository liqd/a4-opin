from django.contrib import admin

from . import models

admin.site.register(models.Offlinephase)
admin.site.register(models.FileUpload)
admin.site.register(models.OfflineEvent)
admin.site.register(models.OfflineEventFileUpload)
