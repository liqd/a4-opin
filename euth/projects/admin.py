from django.contrib import admin

from . import models


class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ('moderators', 'participants')


admin.site.register(models.Project, ProjectAdmin)
