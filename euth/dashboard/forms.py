from django import forms

from euth.contrib import widgets
from euth.projects import models as project_models
from euth.user_management import models as user_models


class ProfileForm(forms.ModelForm):
    class Meta:
        model = user_models.User
        fields = ['avatar', 'email']
        widgets = {
            'avatar': widgets.ImageInputWidget()
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = project_models.Project
        fields = ['image', 'name', 'description', 'information', 'is_public']
        widgets = {
            'image': widgets.ImageInputWidget()
        }
