from django.apps import AppConfig


class Config(AppConfig):
    name = 'euth.users'
    label = 'euth_users'

    def ready(self):
        import euth.users.signals  # noqa:F401
