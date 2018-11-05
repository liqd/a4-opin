from django.apps import AppConfig


class Config(AppConfig):
    name = 'euth.ideas'
    label = 'euth_ideas'

    def ready(self):
        import euth.ideas.signals  # noqa:F401
