from django.utils.translation import ugettext as _

from adhocracy4.categories import forms as category_forms
from adhocracy4.maps import widgets

from . import models


class MapIdeaForm(category_forms.CategorizableForm):

    def __init__(self, *args, **kwargs):
        self.settings = kwargs.pop('settings_instance')
        super().__init__(*args, **kwargs)
        self.fields['point'].widget = widgets.MapChoosePointWidget(
            polygon=self.settings.polygon)
        self.fields['point'].error_messages['required'] = _(
            'Please locate your proposal on the map.')

    class Meta:
        model = models.MapIdea
        fields = ['name', 'description', 'image', 'point']
