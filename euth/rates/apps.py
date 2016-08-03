from django.apps import AppConfig


class RatesConfig(AppConfig):
    name = 'euth.rates'
    label = 'euth_rates'

    def ready(self):
        import euth.rates.signals  # noqa:F401
