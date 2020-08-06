class BookItem:
    reserved_book_items = []

    @classmethod
    def add_issued_books(cls, book):
        cls.reserved_book_items.append(book)

    def __init__(self, book, isbn, rack):
        self.book = book
        self.isbn = isbn
        self.rack = rack
        self.info = {}

    def update_issue_info(self, name, student_id, days):
        self.info["Name"] = name
        self.info["Student ID"] = student_id
        self.info["Days"] = days

    def add_to_issue_list(self):
        BookItem.add_issued_books(self)

    def remove_from_issued_list(self):
        BookItem.reserved_book_items.remove(self)

    def clear_issuer_info(self):
        self.info.clear()
