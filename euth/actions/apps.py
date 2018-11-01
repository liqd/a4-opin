from django.apps import AppConfig


class Config(AppConfig):
    name = 'euth.actions'
    label = 'euth_actions'

    def ready(self):
        import euth.actions.signals  # noqa:F401
