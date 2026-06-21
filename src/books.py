class Book:
    def __init__(self, book_id, title, author, publisher,
                 category, isbn, quantity, available_quantity):

        self.book_id = book_id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.category = category
        self.isbn = isbn
        self.quantity = quantity
        self.available_quantity = available_quantity

    def display_book(self):
        return {
            "Book ID": self.book_id,
            "Title": self.title,
            "Author": self.author,
            "Publisher": self.publisher,
            "Category": self.category,
            "ISBN": self.isbn,
            "Quantity": self.quantity,
            "Available": self.available_quantity
        }

    def issue_book(self):
        if self.available_quantity > 0:
            self.available_quantity -= 1
            return "Book Issued Successfully"
        return "Book Not Available"

    def return_book(self):
        self.available_quantity += 1
        return "Book Returned Successfully"
