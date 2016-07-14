from django.apps import AppConfig


class PhasesConfig(AppConfig):
    name = 'euth.phases'
    label = 'euth_phases'

    def ready(self):
        from django.utils.module_loading import autodiscover_modules
        autodiscover_modules('phases', register_to=self.module.content)
