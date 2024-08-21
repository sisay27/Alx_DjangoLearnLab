# relationship_app/query_samples.py

from .models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = 'Author Name'
specific_author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=specific_author)

# List all books in a library
library_name = 'Library Name'
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

# Retrieve the librarian for a library
librarian_for_library = Librarian.objects.get(library__name=library_name)