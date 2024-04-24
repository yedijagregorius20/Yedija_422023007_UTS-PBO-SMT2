from book import Book
from member import Member

def librarian_menu(library):
    while True:
        print("\nHello, admin! What do you want to do?")
        print("(1) Get all books")
        print("(2) Add book")
        print("(3) Search book")
        print("(4) Manage member information")
        print("(5) Go back")

        librarian_choice = input("\nI want to: ")

        if librarian_choice == "1":
            library.get_all_books()

        elif librarian_choice == "2":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter ISBN Number: ")
            book = Book(title, author, isbn)
            library.add_book(book)

        elif librarian_choice == "3":
            search_option = input("Search by (1) Title or (2) Author? ")
            if search_option == "1":
                title = input("Enter book title: ")
                library.search_books(title=title)
            elif search_option == "2":
                author = input("Enter book author: ")
                library.search_books(author=author)

        elif librarian_choice == "4":
            member_id = input("Enter member ID: ")
            action = input("Choose action (add/update): ")
            if action == "add":
                name = input("Enter member name: ")
                new_member = Member(name, member_id)
                library.manage_member_info(member_id, action=action, new_member=new_member)
            elif action == "update":
                library.manage_member_info(member_id, action=action)

        elif librarian_choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")
