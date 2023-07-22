# books/utils.py
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
# Function to retrieve and return all books
def retrieve_books():
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return serializer.data

def retrieve_book(book_id):
    try:
        book = Book.objects.get(id=book_id)
        serializer = BookSerializer(book)
        return serializer.data
    except Book.DoesNotExist:
        return None

# Function to update a book
def update_book(book_id, new_title, new_author, new_year, new_image):
    try:
        book = Book.objects.get(id=book_id)
        if new_title:
            book.title = new_title
        if new_author:
            book.author = new_author
        if new_year:
            book.year = new_year
        if new_image:
            book.image = new_image
        book.save()
        serializer = BookSerializer(book)
        return serializer.data
    except Book.DoesNotExist:
        return None

# Function to delete a book
def delete_book(book_id):
    try:
        book = Book.objects.get(id=book_id)
        book.delete()
        return True
    except Book.DoesNotExist:
        return False
