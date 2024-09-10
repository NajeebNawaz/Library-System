# Library-System
class Library:
    def __init__(self, book_id, name, author_name, price, quantity):
        self.id = book_id
        self.name = name
        self.author_name = author_name
        self.price = price
        self.quantity = quantity


books = []
total_books = 0

def add_book():
    global total_books
    if total_books < 100:
        book_id = int(input("Enter Book Id: "))
        name = input("Enter Book Name: ")
        author_name = input("Enter Author Name: ")
        price = int(input("Enter Price: "))
        quantity = int(input("Enter Quantity: "))

        new_book = Library(book_id, name, author_name, price, quantity)
        books.append(new_book)
        total_books += 1

def remove_book():
    global total_books
    if total_books > 0:
        book_id = int(input("Enter Book Id: "))
        found = False
        for i, book in enumerate(books):
            if book.id == book_id:
                found = True
                books.pop(i)
                total_books -= 1
                print("Book removed successfully.")
                break
        if not found:
            print("Book not found.")
    else:
        print("No books available to remove.")

def display_books():
    if total_books == 0:
        print("No books to display.")
    else:
        for i, book in enumerate(books):
            print("-------------------")
            print(f"Book Number: {i+1}")
            print(f"Book Id: {book.id}")
            print(f"Book Name: {book.name}")
            print(f"Author Name: {book.author_name}")
            print(f"Book Price: {book.price}")
            print(f"Book Quantity: {book.quantity}")
            print("-------------------")

def library_system():
    while True:
        print("Library System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Display Books")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_book()
        elif choice == 2:
            remove_book()
        elif choice == 3:
            display_books()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the library system
library_system()
