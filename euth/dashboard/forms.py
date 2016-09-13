from betterforms.multiform import MultiModelForm
from django import forms
from django.core.exceptions import ValidationError
from django.forms import modelformset_factory

from euth.contrib import widgets
from euth.modules import models as module_models
from euth.phases import models as phase_models
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


class PhaseCreateForm(forms.ModelForm):

    class Meta:
        model = phase_models.Phase
        exclude = ('module', )
        widgets = {'type': forms.HiddenInput()}


class ProjectCreateForm(forms.ModelForm):

    class Meta:
        model = project_models.Project
        fields = ['image', 'name', 'description', 'information', 'is_public',
                  'result', 'organisation']
        widgets = {
            'image': widgets.ImageInputWidget()
        }


class ProjectCreateMultiForm(MultiModelForm):

    def __init__(self, *args, **kwargs):
        self.extras = kwargs['phase_extras']
        del kwargs['phase_extras']
        super().__init__(*args, **kwargs)

    @property
    def form_classes(self):
        return {
            'project': ProjectCreateForm,
            'phase': modelformset_factory(phase_models.Phase,
                                          PhaseCreateForm,
                                          extra=self.extras)
        }

    def get_form_args_kwargs(self, key, args, kwargs):
        fargs, fkwargs = super().get_form_args_kwargs(key, args, kwargs)
        if key == 'phase':
            queryset = {'queryset': phase_models.Phase.objects.none()}
            queryset.update(fkwargs)
            return (args, queryset)

        return (args, kwargs)

    def is_valid(self):
        forms_valid = all(form.is_valid() for form in self.forms.values())
        try:
            self.clean()
        except ValidationError as e:
            self.add_crossform_error(e)
        # else:
        #    if cleaned_data is not None:
        #        for key, data in cleaned_data.items():
        #            self.forms[key].cleaned_data = data
        return forms_valid and not self.crossform_errors

    def save(self, commit=True):
        objects = super().save(commit=False)

        if commit:
            project = objects['project']
            project.is_draft = False
            project.save()
            module = module_models.Module()
            module.name = project.slug + '_module'
            module.weight = 1
            module.project = project
            module.save()
            phases = objects['phase']
            for phase in phases:
                phase.module = module
                phase.save()

        return objects
