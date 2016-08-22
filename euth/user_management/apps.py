from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'euth.user_management'
    label = 'user_management'

    def ready(self):
        import euth.projects.signals  # noqa:F401
