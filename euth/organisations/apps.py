from django.apps import AppConfig


class Config(AppConfig):
    name = 'euth.organisations'
    label = 'euth_organisations'

    def ready(self):
        import euth.organisations.signals  # noqa:F401
