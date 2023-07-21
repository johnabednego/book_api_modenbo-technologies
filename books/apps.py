# books/apps.py

from django.apps import AppConfig

class BooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'books'

    def ready(self):
        # Import the `insert_books()` function here to avoid AppRegistryNotReady error
        from .utils import insert_books
        insert_books()
