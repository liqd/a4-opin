from django.contrib import admin
from django.urls import reverse

from adhocracy4.modules import models
from adhocracy4.modules.admin import ModuleAdmin as A4ModuleAdmin


class ModuleAdmin(A4ModuleAdmin):

    def view_on_site(self, obj):
        return reverse('project-detail', args=[str(obj.project.slug)])


admin.site.unregister(models.Module)
admin.site.register(models.Module, ModuleAdmin)
