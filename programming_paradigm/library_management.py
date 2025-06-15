class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self.books if not book.is_checked_out]
        for book in available_books:
            print(f"{book.title} by {book.author}")

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self.books:
            if book.title == title and not book.is_checked_out:
                book.is_checked_out = True
                return
        print(f"'{title}' is not available for checkout.")

    def return_book(self, title):
        """Return a checked-out book by title."""
        for book in self.books:
            if book.title == title and book.is_checked_out:
                book.is_checked_out = False
                return
        print(f"'{title}' was not checked out.")