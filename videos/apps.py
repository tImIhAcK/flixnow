from django.apps import AppConfig
from django.core.signals import request_finished


class VideosConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "videos"
    
    def ready(self) -> None:
        import videos.signals
