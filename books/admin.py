from django.contrib import admin

# Register your models here.
# books/admin.py

from django.contrib import admin
from .models import Book

admin.site.register(Book)
