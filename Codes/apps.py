from django.apps import AppConfig


class CodesConfig(AppConfig):
    name = 'Codes'

    def ready(self):
        import Codes.signals
