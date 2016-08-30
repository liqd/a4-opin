from django import forms

from euth.contrib import widgets

from . import models


class IdeaForm(forms.ModelForm):
    class Meta:
        model = models.Idea
        fields = ['name', 'description', 'image']
        widgets = {
            'image': widgets.ImageInputWidget()
        }
