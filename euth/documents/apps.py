from django.apps import AppConfig


class DocumentConfig(AppConfig):
    name = 'euth.documents'
    label = 'euth_documents'

    def ready(self):
        import euth.documents.signals  # noqa:F401
