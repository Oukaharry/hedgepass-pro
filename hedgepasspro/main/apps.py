from django.apps import AppConfig

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'  # Should match directory name
    label = 'main'  # Explicitly set if needed