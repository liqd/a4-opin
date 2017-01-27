from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.forms import modelformset_factory

from contrib.multiforms import multiform

from . import models as offlinephase_models


class OfflinephaseForm(forms.ModelForm):

    class Meta:
        model = offlinephase_models.Offlinephase
        fields = ['text']

    widgets = {
        'text': CKEditorUploadingWidget(
            config_name='image-editor')
    }


class FileUploadForm(forms.ModelForm):

    class Meta:
        model = offlinephase_models.FileUpload
        fields = ['title', 'document']


class OfflinephaseMultiForm(multiform.MultiModelForm):

    base_forms = [
        ('offlinephase', OfflinephaseForm),
        ('fileuploads', modelformset_factory(
            offlinephase_models.FileUpload,
            FileUploadForm, extra=1, max_num=5
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
