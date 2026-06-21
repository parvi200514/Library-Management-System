class Book:
    def __init__(self, title, author, publisher, category, isbn, quantity):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.category = category
        self.isbn = isbn
        self.quantity = quantity

    def add_book(self):
        return f"Book '{self.title}' added successfully."
