from django import forms
from django.utils.translation import gettext_lazy as _

from adhocracy4.forms.fields import DateTimeField
from euth.contrib import widgets

from . import models


class OfflineEventForm(forms.ModelForm):

    date = DateTimeField(
        time_format='%H:%M',
        required=True,
        require_all_fields=False,
        label=(_('Date'), _('Time'))
    )

    class Meta:
        model = models.OfflineEvent
        fields = ['name', 'date', 'description']


class FileUploadForm(forms.ModelForm):

    class Meta:
        model = models.OfflineEventFileUpload
        fields = ['title', 'document']
        widgets = {
            'document': widgets.FileUploadWidget()
        }
