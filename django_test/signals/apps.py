from django.apps import AppConfig


class SignalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signals'
    # for signal
    def ready(self):
        import signals.signal