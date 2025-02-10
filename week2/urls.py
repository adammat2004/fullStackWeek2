from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="index"),
   path('all_books/', views.view_all_books, name="all_books"),
   path('single_book/<int:book_id>/', views.view_single_book, name="single_book"),
   path('books_by_category/<str:category>/', views.view_books_by_category, name="books_by_category"),
]
