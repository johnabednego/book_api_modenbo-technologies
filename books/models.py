# books/models.py

from django.db import models

class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    year = models.IntegerField()

    def __str__(self):
        return self.title
