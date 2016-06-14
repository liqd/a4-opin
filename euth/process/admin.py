from django.contrib import admin

from . import models

class ProcessAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(models.Process, ProcessAdmin)
admin.site.register(models.ParticipationModule)
admin.site.register(models.Phase)
