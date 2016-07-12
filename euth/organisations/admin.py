from parler.admin import TranslatableAdmin, TranslatableModelForm

from django.contrib import admin

from euth.organisations import models


class OrganisationAdmin(TranslatableAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(models.Organisation, OrganisationAdmin)
