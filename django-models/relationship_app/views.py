from django.shortcuts import render
from .models import Book
from django.views.generic import ListView
from .models import Library

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(ListView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
# Create your views here.
