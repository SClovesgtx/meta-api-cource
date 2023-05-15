from django.urls import path
from . import views

urlpatterns = [
    # path('books/', views.books, name='books')
    path("books", views.BookList.as_view()),
    path("book/<int:pk>", views.Book.as_view()),
]
