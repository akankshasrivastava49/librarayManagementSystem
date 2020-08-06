from BookItem import BookItem


class Book:

    def __init__(self, title, author, publication_date):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.total_count = 0
        self.book_item = []

    def add_book_item(self, isbn, rack):
        b = BookItem(self, isbn, rack)
        self.book_item.append(b)
        self.total_count += 1

    def print_book(self):
        print(self.title, self.author)
        for book_item in self.book_item:
            print(book_item.isbn, book_item.rack)

    def view_issued_book_items(self):
        if len(BookItem.reserved_book_items) >= 1:
            for item in BookItem.reserved_book_items:
                print(item.isbn)
        else:
            print("No books are reserved ")

    def view_issue_info(isbn):
        for book_item in BookItem.reserved_book_items:
            if book_item.isbn == isbn:
                print("Issued by: " + book_item.info["Name"])
                print("Student ID: " + book_item.info["Student ID"])
                print("Issued for: " + str(book_item.info["Days"]) + " days")

    def view_issued_bookitems(self):
        if len(BookItem.reserved_book_items) >= 1:
            for item in BookItem.reserved_book_items:
                print(item.isbn)
        else:
            print("No books are issued")

    def update_member_issue_info(book_item, name, student_id, days):
        BookItem.update_issue_info(book_item, name, student_id, days)

    def add_to_issue_list(book_item):
        BookItem.add_to_issue_list(book_item)

    def clear_member_issue_info(book_item):
        BookItem.clear_issuer_info(book_item)

    def remove_from_issue_list(book_item):
        BookItem.remove_from_issued_list(book_item)
