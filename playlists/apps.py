from django.apps import AppConfig


class PlaylistsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "playlists"

    def ready(self) -> None:
        import playlists.signals