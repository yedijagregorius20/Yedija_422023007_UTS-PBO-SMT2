class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __repr__(self):
        available_text = 'Available' if self.available else 'Not Available'
        return f"\nBook Title: {self.title}\nBook Author: {self.author}\nISBN Number: {self.isbn}\nAvailability: {available_text}"

    def set_availability(self, is_available: bool):
        self.available = is_available

    def print_log(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self.available
        }
