
from datetime import datetime


class Book:
    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total = quantity
        self.available = quantity


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name


class Transaction:
    def __init__(self, tid, book_id, member_id):
        self.tid = tid
        self.book_id = book_id
        self.member_id = member_id
        self.issued_at = datetime.now()
        self.returned_at = None


class LibraryManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, "books"):
            return
        self.books = {}
        self.members = {}
        self.transactions = []
        self.next_id = 1

    def add_book(self):
        book_id = input("Enter Book ID: ").strip()
        title = input("Enter Title: ").strip()
        author = input("Enter Author: ").strip()
        quantity = int(input("Enter Quantity: "))

        if not book_id or not title or not author or quantity < 1:
            raise ValueError("Invalid book details.")

        if book_id in self.books:
            raise ValueError("Book ID already exists.")

        self.books[book_id] = Book(book_id, title, author, quantity)
        print("Book added successfully.")

    def register_member(self):
        member_id = input("Enter Member ID: ").strip()
        name = input("Enter Member Name: ").strip()

        if not member_id or not name:
            raise ValueError("Enter valid member details.")

        if member_id in self.members:
            raise ValueError("Member ID already exists.")

        self.members[member_id] = Member(member_id, name)
        print("Member registered successfully.")

    def issue_book(self):
        book_id = input("Enter Book ID: ").strip()
        member_id = input("Enter Member ID: ").strip()

        if book_id not in self.books:
            raise ValueError("Book not found.")

        if member_id not in self.members:
            raise ValueError("Member not found.")

        book = self.books[book_id]

        if book.available == 0:
            raise ValueError("No available copies.")

        for t in self.transactions:
            if (t.book_id == book_id and
                    t.member_id == member_id and
                    t.returned_at is None):
                raise ValueError("Book already issued to this member.")

        book.available -= 1

        transaction = Transaction(
            self.next_id, book_id, member_id
        )

        self.transactions.append(transaction)
        self.next_id += 1

        print("Book issued successfully.")

    def return_book(self):
        tid = int(input("Enter Transaction ID: "))

        transaction = next(
            (t for t in self.transactions if t.tid == tid),
            None
        )

        if transaction is None or transaction.returned_at:
            raise ValueError("Invalid active transaction.")

        self.books[transaction.book_id].available += 1
        transaction.returned_at = datetime.now()

        print("Book returned successfully.")

    def display_books(self):
        print("\nBOOK DETAILS")
        print("-" * 65)

        for b in self.books.values():
            print(
                b.book_id, b.title, b.author,
                b.total, b.available
            )

    def display_members(self):
        print("\nMEMBER DETAILS")
        print("-" * 40)

        for m in self.members.values():
            print(m.member_id, m.name)

    def display_transactions(self):
        print("\nTRANSACTION HISTORY")
        print("-" * 70)

        for t in self.transactions:
            status = "Returned" if t.returned_at else "Issued"

            print(
                t.tid, t.book_id, t.member_id,
                t.issued_at.strftime("%d-%m-%Y %H:%M:%S"),
                t.returned_at or "-", status
            )

    def menu(self):
        while True:
            print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
            print("1. Add Book")
            print("2. Register Member")
            print("3. Issue Book")
            print("4. Return Book")
            print("5. Display Books")
            print("6. Display Members")
            print("7. Transaction History")
            print("8. Verify Singleton")
            print("9. Exit")

            choice = input("Enter your choice: ")

            try:
                if choice == "1":
                    self.add_book()
                elif choice == "2":
                    self.register_member()
                elif choice == "3":
                    self.issue_book()
                elif choice == "4":
                    self.return_book()
                elif choice == "5":
                    self.display_books()
                elif choice == "6":
                    self.display_members()
                elif choice == "7":
                    self.display_transactions()
                elif choice == "8":
                    a = LibraryManager()
                    b = LibraryManager()
                    print("Singleton Verified:", a is b)
                elif choice == "9":
                    print("Exiting Library System.")
                    break
                else:
                    print("Invalid choice.")

            except ValueError as error:
                print("Error:", error)


if __name__ == "__main__":
    library = LibraryManager()
    library.menu()
