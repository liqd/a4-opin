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


class ExtendedProjectForm(ProjectForm):

    invites = forms.CharField(required=False)

    class Meta(ProjectForm.Meta):
        fields = ProjectForm.Meta.fields + ['invites']

    def save(self):
        self.instance.is_draft = 'save_draft' in self.cleaned_data
        return super().save()
