def member_menu(library):
    while True:
        print("\nWelcome! What do you want to do?")
        print('(1) See all books')
        print("(2) Search for books")
        print("(3) Borrow book")
        print("(4) Return book")
        print("(5) Go back")

        member_choice = input("I want to: ")

        if member_choice == "1":
            library.get_all_books()

        elif member_choice == "2":
            search_option = input("Search by (1) Title or (2) Author? ")
            if search_option == "1":
                title = input("Enter book title: ")
                library.search_books(title=title)
            elif search_option == "2":
                author = input("Enter book author: ")
                library.search_books(author=author)

        elif member_choice == "3":
            member_id = input("Enter your member ID: ")
            member = next((m for m in library.members if m.member_id == member_id), None)
            if member:
                isbn = input("Enter book ISBN: ")
                book = next((b for b in library.books if b.isbn == isbn), None)
                if book:
                    library.borrow_book(member, book)
                else:
                    print("Book not found.")
            else:
                print("Member not found.")

        elif member_choice == "4":
            member_id = input("Enter your member ID: ")
            member = next((m for m in library.members if m.member_id == member_id), None)
            if member:
                isbn = input("Enter book ISBN: ")
                book = next((b for b in library.books if b.isbn == isbn), None)
                if book:
                    library.return_book(member, book)
                else:
                    print("Book not found.")
            else:
                print("Member not found.")

        elif member_choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")
