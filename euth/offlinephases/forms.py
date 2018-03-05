from django import forms
from django.utils.translation import ugettext_lazy as _

from adhocracy4.forms.fields import DateTimeField

from . import models, widgets


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
