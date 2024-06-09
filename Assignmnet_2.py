
#Assignment_2


class Library:
    def _init_(self):
        self.books = []
        self.genres = {}

    def add_book(self, title, author, genre):
        return (title, author, genre)

    def add_to_library(self, book):
        if book not in self.books:
            self.books.append(book)
            if book[2] in self.genres:
                self.genres[book[2]].append(book)
            else:
                self.genres[book[2]] = [book]
            print(f"Book '{book[0]}' added to the library.")
        else:
            print(f"Book '{book[0]}' already exists in the library.")

    def remove_from_library(self, title):
        removed = False
        for book in self.books:
            if book[0] == title:
                self.books.remove(book)
                self.genres[book[2]].remove(book)
                removed = True
                print(f"Book '{title}' removed from the library.")
                break
        if not removed:
            print(f"Book '{title}' not found in the library.")

    def search_books(self, term):
        matching_books = []
        for book in self.books:
            if term in book[0] or term in book[1]:
                matching_books.append(book)
        return matching_books

    def list_books(self):
        print("All books in the library:")
        for book in self.books:
            print(f"Title: {book[0]}, Author: {book[1]}, Genre: {book[2]}")

    def categorize_books(self):
        print("Categorized books by genre:")
        for genre, books in self.genres.items():
            print(f"Genre: {genre}")
            for book in books:
                print(f"Title: {book[0]}, Author: {book[1]}")

library = Library()

while True:
    print("\nMenu:")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for books")
    print("4. List all books")
    print("5. Categorize books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        genre = input("Enter the genre of the book: ")
        book = library.add_book(title, author, genre)
        library.add_to_library(book)
    elif choice == '2':
        title = input("Enter the title of the book to remove: ")
        library.remove_from_library(title)
    elif choice == '3':
        term = input("Enter the search term (title or author): ")
        result = library.search_books(term)
        if result:
            print("Matching books:")
            for book in result:
                print(f"Title: {book[0]}, Author: {book[1]}, Genre: {book[2]}")
        else:
            print("No matching books found.")
    elif choice == '4':
        library.list_books()
    elif choice == '5':
        library.categorize_books()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")