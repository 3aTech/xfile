from django.apps import AppConfig


class UsuarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuario'
    verbose_name = 'perfiles'
    
    def ready(self) -> None:
        import usuario.signals