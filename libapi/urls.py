from django.urls import path
from .views import BooksDetail,BooksList,BorrowedsList,BorrowedDetail

urlpatterns = [
    #users - post and get all
    path('books', BooksList.as_view(),name='books'),
    #users get by id , update delete
    path('book/<int:pk>/', BooksDetail.as_view(),name='books-details'),
    #users - post and get all
    path('borrowed', BorrowedsList.as_view(),name='books-borrowed'),
    #users get by id , update delete
    path('borrowed/<int:pk>/', BorrowedDetail.as_view(),name='books=borrowed-details'),
]
