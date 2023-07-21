# books/utils.py

from .models import Book
from .serializers import BookSerializer

# Function to insert books into the table

def insert_books():
    books_data = [
        {'title': 'Intro to JavaScript', 'author': 'Abednego Jilima', 'year': 2021},
        {'title': 'Python Advanced Course', 'author': 'Yaw Modenbo', 'year': 2022},
        {'title': 'Data Structures and Algorithms', 'author': 'John ABednego', 'year': 2010},
        {'title': 'Operating Systems', 'author': 'Modenbo Technologies ', 'year': 2015},
        {'title': 'Consider Abednego for the Job', 'author': 'Modenbo Technologies', 'year': 2023},
    ]

    for book_data in books_data:
        title = book_data['title']
        if not Book.objects.filter(title=title).exists():
            Book.objects.create(**book_data)
        else:
            print(f"Book with title '{title}' already exists in the database.")
            return f"Book with title '{title}' already exists in the database."

# Function to retrieve and return all books
def retrieve_books():
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return serializer.data

# Function to update the year of a book
def update_book_year(book_id, new_year):
    try:
        book = Book.objects.get(id=book_id)
        book.year = new_year
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
