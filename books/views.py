# books/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import insert_books, retrieve_books, update_book_year, delete_book
from .serializers import BookSerializer

@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = retrieve_books()
        return Response(books)

    elif request.method == 'POST':
        insert_books()
        return Response({'message': 'Books created successfully.'})

@api_view(['PUT', 'DELETE'])
def book_detail(request, book_id):
    if request.method == 'PUT':
        new_year = 2025  # Set the new year as per your requirement
        updated_book = update_book_year(book_id, new_year)
        if updated_book:
            return Response({'message': f'Book with id={book_id} updated successfully.'})
        else:
            return Response({'error': f'Book with id={book_id} not found.'}, status=404)

    elif request.method == 'DELETE':
        deleted = delete_book(book_id)
        if deleted:
            return Response({'message': f'Book with id={book_id} deleted successfully.'})
        else:
            return Response({'error': f'Book with id={book_id} not found.'}, status=404)
