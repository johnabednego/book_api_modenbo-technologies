# books/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import retrieve_books, update_book, delete_book, retrieve_book
from .models import Book

@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = retrieve_books()
        return Response(books)
    elif request.method == 'POST':
        new_id = len(retrieve_books())+1
        new_title = request.data.get('title')
        new_author = request.data.get('author')
        new_year = request.data.get('year')
        new_image = request.FILES['image']
        if new_title is None or new_author is None or new_year is None or new_image is None:
            return Response({'error': "All fields are Required!!!"}, status=400)
        else:
            # Save the image to the database
            if not Book.objects.filter(title=new_title).exists():
                book = Book.objects.create(id=new_id, title=new_title, author=new_author, year=new_year, image=new_image)
                return Response({'message': f'Book with id={book.id} created successfully.'}, status=201)
            else:
                return Response({'message': f"Book with title '{new_title}' already exists in the database."}, status=400) 
            
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
        
        # Handle image upload directly here
        new_image = request.FILES.get('image')  # Access the uploaded image file
        
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
