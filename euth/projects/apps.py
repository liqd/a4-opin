from django.apps import AppConfig


class Config(AppConfig):
    name = 'euth.projects'
    label = 'euth_projects'

    def ready(self):
        import euth.projects.signals  # noqa
