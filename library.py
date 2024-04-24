from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Book added successfully!")

    def add_member(self, member: Member):
        self.members.append(member)
        print(f"Member added successfully!")

    def get_all_books(self):
        results = [
            book for book in self.books
        ]

        if results:
            print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("====== Search Results: ======")
            print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
            for book in results:
                print(book)
        else:
            print("No books found.")

    def search_books(self, title: str = None, author: str = None):
        results = [
            book for book in self.books
            if (title and title.lower() in book.title.lower()) or
               (author and author.lower() in book.author.lower())
        ]

        if results:
            print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("====== Search Results: ======")
            print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+')
            for book in results:
                print(book)
        else:
            print("No books found.")

    def borrow_book(self, member: Member, book: Book):
        if book in self.books and member in self.members:
            member.borrow_book(book)
        else:
            print("Invalid book or member.")

    def return_book(self, member: Member, book: Book):
        if book in self.books and member in self.members:
            member.return_book(book)
        else:
            print("Invalid book or member.")

    def manage_member_info(self, member_id: str = None, action: str = None, new_member: Member = None):
        if action == 'add' and new_member:
            self.add_member(new_member)
        elif action == 'update' and member_id:
            member = next((m for m in self.members if m.member_id == member_id), None)
            if member:
                print(f"Member Info: {member.print_log()}")
                new_name = input("Enter new member's name: ")
                if new_name:
                    member.name = new_name
                    print("Member info updated!")
            else:
                print("Member not found.")