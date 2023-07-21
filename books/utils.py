# books/utils.py
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

# Function to insert books into the table
def insert_books():
    books_data = [
        {'id': 1, 'title': 'Intro to JavaScript', 'author': 'Abednego Jilima', 'year': 2021},
        {'id': 2, 'title': 'Python Advanced Course', 'author': 'Yaw Modenbo', 'year': 2022},
        {'id': 3, 'title': 'Data Structures and Algorithms', 'author': 'John ABednego', 'year': 2010},
        {'id': 4, 'title': 'Operating Systems', 'author': 'Modenbo Technologies ', 'year': 2015},
        {'id': 5, 'title': 'Consider Abednego for the Job', 'author': 'Modenbo Technologies', 'year': 2023},
    ]

    for book_data in books_data:
        title = book_data['title']
        if not Book.objects.filter(title=title).exists():
            Book.objects.create(**book_data)
            Response({'message': 'Books created successfully.'})
        else:
            return Response({'message': f"Book with title '{title}' already exists in the database."}) 

# Function to retrieve and return all books
def retrieve_books():
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return serializer.data

# Function to insert a book into the table
def insert_book(new_title, new_author, new_year):
    if not Book.objects.filter(title=new_title).exists():
        book_data =  {'id': len(retrieve_books())+1,'title': new_title, 'author': new_author, 'year': new_year}
        Book.objects.create(**book_data)
        return Response({'Book':book_data, 'message': 'Book was created successfully.'})
    else:
        return Response({'message': f"Book with title '{new_title}' already exists in the database."}) 


def retrieve_book(book_id):
    try:
        book = Book.objects.get(id=book_id)
        serializer = BookSerializer(book)
        return serializer.data
    except Book.DoesNotExist:
        return None

# Function to update a book
def update_book(book_id, new_title, new_author, new_year):
    try:
        book = Book.objects.get(id=book_id)
        if new_title:
            book.title = new_title
        if new_author:
            book.author = new_author
        if new_year:
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
