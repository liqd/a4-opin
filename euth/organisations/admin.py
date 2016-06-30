from django.contrib import admin

from . import models


class OrganisationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(models.Organisation, OrganisationAdmin)
