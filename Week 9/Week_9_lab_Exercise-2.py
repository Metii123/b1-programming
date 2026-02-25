class Book:
    def __init__(self, title, author, isbn):
        self.title  = title
        self.author = author
        self.isbn   = isbn

    def display(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"


class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)
        print(f"[LOG]: Added - {book.display()}")

    def remove_book(self, title):
        book = self.search(title)
        if book:
            self.__books.remove(book)
            print(f"[LOG]: Removed - '{title}'.")
        else:
            print(f"[LOG]: '{title}' not found.")

    def list_books(self):
        if not self.__books:
            print("[LOG]: No books in library.")
        for book in self.__books:
            print(f"  - {book.display()}")

    def search(self, title):
        for book in self.__books:
            if book.title.lower() == title.lower():
                print(f"[LOG]: Found - {book.display()}")
                return book
        print(f"[LOG]: '{title}' not found.")
        return None


if __name__ == "__main__":
    library = Library()

    library.add_book(Book("1984",              "George Orwell",   "978-0451524935"))
    library.add_book(Book("The Great Gatsby",  "F. Scott Fitzgerald", "978-0743273565"))
    library.add_book(Book("Hard Times",        "Charles Dickens", "978-0141439679"))

    print("\n--- All books ---")
    library.list_books()

    print("\n--- Search ---")
    library.search("1984")

    print("\n--- Remove ---")
    library.remove_book("The Great Gatsby")

