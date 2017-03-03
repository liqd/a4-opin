from django import forms
from django.forms import modelformset_factory

from contrib.multiforms import multiform

from . import models as offlinephase_models
from . import widgets


class OfflinephaseForm(forms.ModelForm):
    class Meta:
        model = offlinephase_models.Offlinephase
        fields = ['text']


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = offlinephase_models.FileUpload
        fields = ['title', 'document']
        widgets = {
            'document': widgets.FileUploadWidget()
        }


class OfflinephaseMultiForm(multiform.MultiModelForm):
    base_forms = [
        ('offlinephase', OfflinephaseForm),
        ('fileuploads', modelformset_factory(
            offlinephase_models.FileUpload,
            FileUploadForm, extra=1, max_num=5, can_delete=True
        )),
    ]

    def save(self, commit=True):

        objects = super().save(commit=False)
        offlinephase = objects['offlinephase']
        fileuploads = objects['fileuploads']

        if commit:
            offlinephase.save()

        for fileupload in fileuploads:
            fileupload.offlinephase = offlinephase
            if commit:
                fileupload.save()

        if commit:
            cleaned_data = self._combine('cleaned_data', call=False,
                                         call_kwargs={'commit': commit})
            fileuploads_cleaned = cleaned_data['fileuploads']

            for fu in fileuploads_cleaned:
                if 'DELETE' in fu and fu['DELETE']:
                    fu['id'].delete()
