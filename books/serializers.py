# books/serializers.py

from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)  
    class Meta:
        model = Book
        fields = '__all__'
