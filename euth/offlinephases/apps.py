from django.apps import AppConfig


class OfflinephaseConfig(AppConfig):
    name = 'euth.offlinephases'
    label = 'euth_offlinephases'

    def ready(self):
        import euth.offlinephases.signals  # noqa:F401
