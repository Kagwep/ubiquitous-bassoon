from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Books,Borrowed
from .serializers import BooksSerializer,BorrowedSerializer

#get all users / post new user
class BooksList(APIView):

    def get(self, request):
        #get all users from model
        books = Books.objects.all()
        #serialize our user objects
        serializer = BooksSerializer(books, many=True)
        #return serialized data
        return Response(serializer.data)

    def post(self, request):
        # print('hello')
        # print(request.data)
        #use our serializer class to serialize data from request
        serializer = BooksSerializer(data=request.data)
        # print(serializer)
        #if valid
        if serializer.is_valid():
            #save object
            serializer.save()
            #return the data 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #if not return status and the reason
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BooksDetail(APIView):

    # Retrieve, update or delete a user instance

    #get user
    def get_object(self, pk):
        try:
            return Books.objects.get(id=pk)
        except Books.DoesNotExist:
            raise Http404
        
     #get user by id
    def get(self, request, pk):
        book = Books.objects.get(id=pk)
        serializer = BooksSerializer(book)
        return Response(serializer.data)

 
    #update the fields of requested object id
    def put(self, request, pk):
        book = Books.objects.get(id=pk)

        # Only update fields that were provided
        if 'book_name' in request.data:
            book.book_name = request.data['book_name']
        if 'author' in request.data:
            book.author = request.data['author']


        #save the update
        book.save()

         #serialize the user
        serializer = BooksSerializer(book)
         # return the updated data
        return Response(serializer.data)

    #get the user by id
    def delete(self, request, pk):
        book = Books.objects.get(id=pk)
        #delete the user
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#get all users / post new user
class BorrowedsList(APIView):

    def get(self, request):
        #get all users from model
        borrowed = Borrowed.objects.all()
        #serialize our user objects
        serializer = BorrowedSerializer(borrowed, many=True)
        #return serialized data
        return Response(serializer.data)

    def post(self, request):
        # print('hello')
        # print(request.data)
        #use our serializer class to serialize data from request
        serializer = BorrowedSerializer(data=request.data)
        # print(serializer)
        #if valid
        if serializer.is_valid():
            #save object
            serializer.save()
            #return the data 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #if not return status and the reason
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BorrowedDetail(APIView):

    # Retrieve, update or delete a user instance

    #get user
    def get_object(self, pk):
        try:
            return Borrowed.objects.get(id=pk)
        except Borrowed.DoesNotExist:
            raise Http404
        
     #get user by id
    def get(self, request, pk):
        borrowed = Borrowed.objects.get(id=pk)
        serializer = BorrowedSerializer(borrowed)
        return Response(serializer.data)

 
    #update the fields of requested object id
    def put(self, request, pk):
        borrowed= Borrowed.objects.get(id=pk)

        # Only update fields that were provided
        if 'name' in request.data:
            borrowed.name = request.data['name']
        if 'book' in request.data:
            borrowed.book = request.data['book']


        #save the update
        borrowed.save()

         #serialize the user
        serializer = BooksSerializer(borrowed)
         # return the updated data
        return Response(serializer.data)

    #get the user by id
    def delete(self, request, pk):
        Borrowed = Borrowed.objects.get(id=pk)
        #delete the user
        Borrowed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)