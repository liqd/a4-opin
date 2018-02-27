from django.apps import AppConfig


class Config(AppConfig):
    name = 'euth.exports'
    label = 'euth_exports'

    def ready(self):
        from django.utils.module_loading import autodiscover_modules
        autodiscover_modules('exports', register_to=self.module.exports)
