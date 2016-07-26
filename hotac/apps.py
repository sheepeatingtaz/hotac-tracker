from django.apps import AppConfig


class HotacConfig(AppConfig):
    name = 'hotac'

    def ready(self):
        from . import signals