from django import forms

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
