from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    name = 'euth.projects'
    label = 'euth_projects'

    def ready(self):
        import euth.projects.signals  # noqa:F401
