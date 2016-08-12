from django.apps import AppConfig


class ReportConfig(AppConfig):
    name = 'euth.reports'
    label = 'euth_reports'

    def ready(self):
        import euth.reports.signals  # noqa:F401
