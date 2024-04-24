from library import Library
from book import Book
from member import Member
from librarian_menu import librarian_menu
from member_menu import member_menu

def main():
    library = Library()

    # Add some initial books and members
    library.add_book(Book("Web Progamming Fundamental4", "Gregor", "ISBN001"))
    library.add_book(Book("Internet of Things", "Jack Sparrow", "ISBN002"))

    library.add_member(Member("Erlangga", "MEM001"))
    library.add_member(Member("Dani", "MEM002"))

    while True:
        print("\n------------------------------")
        print("====== UKRIDA E-Library ======")
        print("------------------------------")
        print("What is your role?\n(1) Librarian\n(2) Member")
        print("\nPress (0) to Quit")

        choice = input("\nMy role is: ")

        if choice == "1":
            librarian_menu(library)

        elif choice == "2":
            member_menu(library)

        elif choice == "0":
            print("Happy reading!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
