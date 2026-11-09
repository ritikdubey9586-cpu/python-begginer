class Library:
    def __init__(self):
        # Instance variables initialized
        self.books = []
        self.no_of_books = 0

    def add_book(self, book_title):
        """Adds a new book to the library and updates the count."""
        # Convert to title case for consistent formatting
        formatted_title = book_title.strip().title()
        
        if not formatted_title:
            print(" Book title cannot be empty!")
            return
            
        if formatted_title in self.books:
            print(f"'{formatted_title}' is already in the library.")
            return

        self.books.append(formatted_title)
        self.no_of_books = len(self.books)
        print(f"Added: '{formatted_title}'")

    def remove_book(self, book_title):
        """Removes a book from the library if it exists."""
        formatted_title = book_title.strip().title()
        
        if formatted_title in self.books:
            self.books.remove(formatted_title)
            self.no_of_books = len(self.books)
            print(f"Removed: '{formatted_title}'")
        else:
            print(f"'{formatted_title}' not found in the library.")

    def show_books(self):
        """Displays all available books and confirms the internal count matches."""
        if self.no_of_books == 0:
            print("\nThe library is currently empty.")
            return

        # Verification check to ensure instance variables stay in sync
        if self.no_of_books != len(self.books):
            print(" Warning: Book count mismatch detected!")
            
        print(f"\n Library Catalogue ({self.no_of_books} Total Books):")
        for idx, book in enumerate(self.books, 1):
            print(f"  {idx}. {book}")


def main():
    # Instantiate the library object
    my_library = Library()
    
    # Pre-populating some initial books
    initial_books = ["The Python Workbook", "To Kill a Mockingbird", "1984"]
    for book in initial_books:
        my_library.add_book(book)

    while True:
        print("\n---  Library Management System ---")
        print("1. View All Books")
        print("2. Add a Book")
        print("3. Remove a Book")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == "1":
            my_library.show_books()
        elif choice == "2":
            title = input("Enter the title of the book to add: ")
            my_library.add_book(title)
        elif choice == "3":
            title = input("Enter the title of the book to remove: ")
            my_library.remove_book(title)
        elif choice == "4":
            print("Goodbye! Closing the library system.")
            break
        else:
            print(" Invalid option. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()
