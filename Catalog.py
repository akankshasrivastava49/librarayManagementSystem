# -*- coding: utf-8 -*-
from Book import Book
class Catalog:
    books_list = []
    different_book_count = 0

    @classmethod
    def add_books_list(cls, book):
        cls.books_list.append(book)

    def add_book(title, author, publication_date):
        b = Book(title, author, publication_date)
        Catalog.add_books_list(b)
        Catalog.different_book_count += 1

    def add_book_item(title, isbn, rack):
        for book in Catalog.books_list:
            if book.title == title:
                Book.add_book_item(book, isbn, rack)
                print("Book added")

    def remove_book(rem_book):
        for book in Catalog.books_list:
            if book.title == rem_book:
                Catalog.books_list.remove(book)
                Catalog.different_book_count -= 1
                print("Book removed")

    def remove_book_item(rem_bookitem):
        for book in Catalog.books_list:
            for book_item in book.book_item:
                if book_item.isbn == rem_bookitem:
                    book.book_item.remove(book_item)
                    book.total_count -= 1
                    print("Book item removed")

    def search_by_book_name(title):
        for book in Catalog.books_list:
            if book.title == title:
                print(f"{book.title} is available!")
                break
        else:
            print(f"Sorry {title} is currently not available")

    def search_by_author_name(author):
        count = 0
        for book in Catalog.books_list:
            if book.author == author:
                print(book.title)
                count += 1
        if count == 0:
            print(f"Sorry , books written by {author} is not available")

    def display_all_books(self):
        c = 0
        for book in Catalog.books_list:
            c += book.total_count
            book.print_book()
        print("Different Book Count", Catalog.different_book_count)
        print("Total Book Count", c)

    def update_member_issue_info(book_item, name, student_id, days):
        Book.update_member_issue_info(book_item, name, student_id, days)

    def add_to_issue_list(book_item):
        Book.add_to_issue_list(book_item)

    def clear_member_issue_info(ret_book_item):
        Book.clear_member_issue_info(ret_book_item)

    def remove_from_issue_list(ret_book_item):
        Book.remove_from_issue_list(ret_book_item)

    def view_issued_bookitems(self):
        Book.view_issued_bookitems(self)
class IssueReturn:

    def issue_book(name, student_id, book_title, days):
        for book in Catalog.books_list:
            if book.title == book_title and len(book.book_item) != 0:
                book_item = book.book_item.pop()
                book.total_count -= 1
                Catalog.update_member_issue_info(book_item, name, student_id, days)
                Catalog.add_to_issue_list(book_item)
                return book_item
        else:
            print(f"{book_title} is currently not available in the library")

    def return_book(return_book_item):
        for book in Catalog.books_list:
            if book == return_book_item:
                book.book_item.append(return_book_item)
                book.total_count += 1
        Catalog.clear_member_issue_info(return_book_item)
        Catalog.remove_from_issue_list(return_book_item)