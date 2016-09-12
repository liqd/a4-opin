from django.contrib import admin
from parler.admin import TranslatableAdmin

from euth.organisations import models


class OrganisationAdmin(TranslatableAdmin):
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ('initiators',)


admin.site.register(models.Organisation, OrganisationAdmin)
