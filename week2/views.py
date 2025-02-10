from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def view_all_books(request):
   all_books = Book.objects.all()
   return render(request, 'all_books.html', {'books': all_books})

def view_single_book(request, book_id):
   single_book = get_object_or_404(Book, id=book_id)
   return render(request, 'single_book.html', {'book': single_book})

def view_books_by_category(request, category):
   books_by_category = Book.objects.filter(category=category)
   return render(request, 'books_by_category.html', {'books': books_by_category})