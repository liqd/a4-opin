from django.apps import AppConfig


class Config(AppConfig):
    name = 'euth.communitydebate'
    label = 'euth_communitydebate'

    def ready(self):
        import euth.communitydebate.signals  # noqa:F401
