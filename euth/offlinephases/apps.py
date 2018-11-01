from django.apps import AppConfig


class Config(AppConfig):
    name = 'euth.offlinephases'
    label = 'euth_offlinephases'

    def ready(self):
        import euth.offlinephases.signals  # noqa:F401
