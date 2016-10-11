from django.apps import AppConfig


class FakeProjectsConfig(AppConfig):
    """Implement app that fakes the view of projects."""
    name = 'tests.apps.fakeprojects'
    label = 'fakeprojects'
