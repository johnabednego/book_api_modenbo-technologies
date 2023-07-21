# books/models.py

from django.db import models

class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    author = models.TextField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='books/images')

    def __str__(self):
        return self.title
