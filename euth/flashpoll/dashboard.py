from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from adhocracy4.dashboard import (DashboardComponent, ModuleFormComponent,
                                  components)

from . import forms, views


class FlashpollComponent(ModuleFormComponent):
    identifier = 'flashpoll_settings'
    weight = 12

    label = _('Flashpollsettings')
    form_title = _('Edit flashpollsettings')
    form_class = forms.FlashpollSettingsForm
    form_template_name = 'euth_flashpoll/includes/flashpoll_form.html'

    def is_effective(self, module):
        phase = module.phases[0]
        module_settings = module.settings_instance
        return module_settings and \
            hasattr(module_settings, 'key') and \
            phase.start_date and phase.end_date

    def get_progress(self, module):
        module_settings = module.settings_instance
        if module_settings:
            return super().get_progress(module_settings)
        return 0, 0


class FlashpollAnswersExportComponent(DashboardComponent):
    identifier = 'flashpoll_aswers_export'
    weight = 20
    label = _('Answers and Export')

    def is_effective(self, module):
        module_settings = module.settings_instance
        return module_settings and \
            hasattr(module_settings, 'key') and not \
            module_settings.key == ''

    def get_base_url(self, module):
        return reverse('a4dashboard:flashpoll-export', kwargs={
            'module_slug': module.slug
        })

    def get_urls(self):
        return [
            (r'^flashpoll-export/module/(?P<module_slug>[-\w_]+)/$',
             views.FlashpollExportView.as_view(component=self),
             'flashpoll-export'),
        ]


components.register_module(FlashpollComponent())
components.register_module(FlashpollAnswersExportComponent())
