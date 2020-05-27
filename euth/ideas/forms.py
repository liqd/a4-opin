from django import forms

from adhocracy4.categories import forms as category_forms
from euth.contrib.mixins import ImageRightOfUseMixin

from . import models


class IdeaForm(category_forms.CategorizableFieldMixin,
               ImageRightOfUseMixin,
               forms.ModelForm):

    class Meta:
        model = models.Idea
        fields = ['name', 'description', 'image', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = '---'
