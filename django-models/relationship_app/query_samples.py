
from .models import Author, Book, Library, Librarian

# Query all books by a specific author
specific_author_books = Book.objects.filter(author__name='Specific Author')

# List all books in a library
library_name = 'Library Name'
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

# Retrieve the librarian for a library
librarian_for_library = Librarian.objects.get(library__name=library_name)