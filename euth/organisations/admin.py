from django.contrib import admin
from parler.admin import TranslatableAdmin

from euth.organisations import models


class OrganisationAdmin(TranslatableAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(models.Organisation, OrganisationAdmin)
