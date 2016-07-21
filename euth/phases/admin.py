from django import forms
from django.contrib import admin

from . import content, models


class PhaseForm(forms.ModelForm):
    type = forms.ChoiceField(choices=content.as_choices)

    class Meta:
        fields = '__all__'
        model = models.Phase


class PhaseAdmin(admin.ModelAdmin):
    form = PhaseForm


admin.site.register(models.Phase, PhaseAdmin)
