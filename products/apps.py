from django.apps import AppConfig
from django.core.cache import caches


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

    def ready(self):
        # Clear the Redis cache on server startup
        try:
            caches['alternate'].clear()  # Clear alternate cache if you use multiple caches
            print("Cache cleared on server restart.")
        except Exception as e:
            print(f"Error clearing cache: {e}")
