# books/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import insert_book, retrieve_books, update_book, delete_book, retrieve_book

@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = retrieve_books()
        return Response(books)
    elif request.method == 'POST':
        new_title = request.data.get('title')
        new_author = request.data.get('author')
        new_year = request.data.get('year')
        new_image = request.data.get('image')
        if new_title is None or new_author is None or new_year is None or new_image is None:
            return Response({'error': "All fields are Required!!!"}, status=400)
        else:
            return  insert_book(new_title, new_author, new_year, new_image)
    else:
        return Response({'error': f'{request.method} Request is not Allowed!!!'}, status=404)

@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, book_id):
    if request.method == 'GET':
        book = retrieve_book(book_id)
        if book:
            return Response(book)
        else:
            return Response({'error': f'Book with id={book_id} not found.'}, status=404)
    elif request.method == 'PUT':
        # Retrieve the new year from the request data
        new_title = request.data.get('title')
        new_author = request.data.get('author')
        new_year = request.data.get('year')
        new_image = request.data.get('image')
        if new_title is None and new_author is None and new_year is None and new_image is None:
            return Response({'error': "All fields can't be Empty!!!"}, status=400)
        else:
            # Call the update_book function
            updated_book = update_book(book_id, new_title, new_author, new_year, new_image)

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
    else:
        return Response({'error': f'{request.method} Request is not Allowed!!!'}, status=404)