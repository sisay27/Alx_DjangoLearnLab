# relationship_app/query_samples.py

from .models import Author, Book, Library, Librarian

# Query all books by a specific author
specific_author_books = Book.objects.filter(author__name='Specific Author')

# List all books in a library
all_books_in_library = Book.objects.filter(library__name='Library Name')

# Retrieve the librarian for a library
librarian_for_library = Librarian.objects.get(library__name='Library Name')