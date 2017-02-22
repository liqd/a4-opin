from django import forms
from django.utils.translation import ugettext as _

from . import models
from .widgets import MapChoosePointWidget


class MapIdeaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.settings = kwargs.pop('settings_instance')
        super().__init__(*args, **kwargs)
        self.fields['point'].widget = MapChoosePointWidget(
            polygon=self.settings.polygon)
        self.fields['point'].error_messages['required'] = _(
            'Please locate your proposal on the map.')

    class Meta:
        model = models.MapIdea
        fields = ['name', 'description', 'image', 'point']
