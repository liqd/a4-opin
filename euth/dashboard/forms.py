from betterforms.multiform import MultiModelForm
from django import forms

from euth.contrib import widgets
from euth.modules import models as module_models
from euth.projects import models as project_models
from euth.users import models as user_models


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
        fields = ['image', 'name', 'description', 'information', 'is_public',
                  'result']
        widgets = {
            'image': widgets.ImageInputWidget()
        }


class ModuleCreateForm(forms.ModelForm):

    class Meta:
        model = module_models.Module
        fields = ['name', 'description', 'weight']


class ProjectCreateForm(forms.ModelForm):

    class Meta:
        model = project_models.Project
        fields = ['image', 'name', 'description', 'information', 'is_public',
                  'result', 'organisation']
        widgets = {
            'image': widgets.ImageInputWidget()
        }


class ProjectCreateMultiForm(MultiModelForm):
    form_classes = {
        'project': ProjectCreateForm,
        'module': ModuleCreateForm
    }
