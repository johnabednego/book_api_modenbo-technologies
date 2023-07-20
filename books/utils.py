# books/utils.py

from .models import Book

# Function to insert books into the table
def insert_books():
    books_data = [
        {'title': 'Book 1', 'author': 'Author 1', 'year': 2000},
        {'title': 'Book 2', 'author': 'Author 2', 'year': 2005},
        {'title': 'Book 3', 'author': 'Author 3', 'year': 2010},
        {'title': 'Book 4', 'author': 'Author 4', 'year': 2015},
        {'title': 'Book 5', 'author': 'Author 5', 'year': 2020},
    ]

    for book_data in books_data:
        Book.objects.create(**book_data)

# Function to retrieve and return all books
def retrieve_books():
    books = Book.objects.all()
    return books

# Function to update the year of a book
def update_book_year(book_id, new_year):
    try:
        book = Book.objects.get(id=book_id)
        book.year = new_year
        book.save()
    except Book.DoesNotExist:
        return None

    return book

# Function to delete a book
def delete_book(book_id):
    try:
        book = Book.objects.get(id=book_id)
        book.delete()
        return True
    except Book.DoesNotExist:
        return False
