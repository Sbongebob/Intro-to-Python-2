class Book:
    def __init__(self, book_id, name, quantity):
        self.id = book_id
        self.name = name
        self.quantity = quantity

    def borrow_book(self):
        if self.quantity > 0:
            self.quantity -= 1
            return True
        return False

    def return_book(self):
        self.quantity += 1

    def check_quantity(self):
        return self.quantity


class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.borrowed_books = []
        self.max_books = 3

    def can_borrow(self):
        return len(self.borrowed_books) < self.max_books

    def borrow_book(self, book_id):
        self.borrowed_books.append(book_id)

    def return_book(self, book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)


class Admin:
    def __init__(self):
        self.books = []
        self.users = []

    # Helper Methods
    def find_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def find_user(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    # Menu Options
    def add_book(self):
        book_id = input("Book ID: ")

        if self.find_book(book_id):
            print("Book ID already exists.")
            return

        name = input("Book Title: ")
        quantity = int(input("Quantity: "))

        self.books.append(Book(book_id, name, quantity))
        print("Book added successfully.")

    def print_library_books(self):
        if not self.books:
            print("No books in library.")
            return

        print("\nLibrary Books")
        for book in self.books:
            print(f"ID: {book.id} | {book.name} | Quantity: {book.quantity}")

    def print_books_by_prefix(self):
        prefix = input("Enter title prefix: ").lower()

        found = False
        for book in self.books:
            if book.name.lower().startswith(prefix):
                print(f"{book.id} - {book.name} ({book.quantity} copies)")
                found = True

        if not found:
            print("No books found.")

    def add_user(self):
        user_id = input("User ID: ")

        if self.find_user(user_id):
            print("User ID already exists.")
            return

        name = input("User Name: ")

        self.users.append(User(user_id, name))
        print("User added successfully.")

    def borrow_book(self):
        user_id = input("User ID: ")
        user = self.find_user(user_id)

        if user is None:
            print("User not found.")
            return

        if not user.can_borrow():
            print("User has reached the maximum number of borrowed books.")
            return

        book_id = input("Book ID: ")
        book = self.find_book(book_id)

        if book is None:
            print("Book not found.")
            return

        if book.borrow_book():
            user.borrow_book(book.id)
            print("Book borrowed successfully.")
        else:
            print("No copies available.")

    def return_book(self):
        user_id = input("User ID: ")
        user = self.find_user(user_id)

        if user is None:
            print("User not found.")
            return

        book_id = input("Book ID: ")

        if book_id not in user.borrowed_books:
            print("This user did not borrow that book.")
            return

        book = self.find_book(book_id)

        if book is not None:
            book.return_book()

        user.return_book(book_id)

        print("Book returned successfully.")

    def print_users(self):
        if not self.users:
            print("No users registered.")
            return

        print("\nUsers")
        for user in self.users:
            print(f"ID: {user.id}")
            print(f"Name: {user.name}")

            if user.borrowed_books:
                print("Borrowed Books:")
                for book_id in user.borrowed_books:
                    book = self.find_book(book_id)
                    if book:
                        print(f" - {book.name}")
            else:
                print("Borrowed Books: None")

            print()

    # ----------------------------
    # Main Menu
    # ----------------------------
    def menu(self):
        while True:
            print("\n===== Library Management System =====")
            print("1. Add Book")
            print("2. Print Library Books")
            print("3. Print Books by Prefix")
            print("4. Add User")
            print("5. Borrow Book")
            print("6. Return Book")
            print("7. Print Users")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.print_library_books()
            elif choice == "3":
                self.print_books_by_prefix()
            elif choice == "4":
                self.add_user()
            elif choice == "5":
                self.borrow_book()
            elif choice == "6":
                self.return_book()
            elif choice == "7":
                self.print_users()
            elif choice == "8":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")


def main():
    admin = Admin()
    admin.menu()


if __name__ == "__main__":
    main()



