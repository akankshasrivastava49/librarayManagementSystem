# -*- coding: utf-8 -*-

from Catalog import Catalog,IssueReturn


class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id

    def viewBooks(self):
        Catalog.display_all_books(self)


class Member(User):
    members_list = []

    @classmethod
    def addMemberList(cls, member):
        cls.members_list.append(member)

    def __init__(self, name, location, age, aadhar_id, student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        self.issued_books_list = []
        Member.addMemberList(self)

    def __repr__(self):
        return self.name + " " + self.location + " " + self.student_id

    def search_by_book_name(self, title):
        Catalog.search_by_book_name(title)

    def search_by_author_name(self, author):
        Catalog.search_by_author_name(author)

    def issue_book(self, book_title, days=10):
        if days <= 10:
            for member in Member.members_list:
                if member == self:
                    book_item = IssueReturn.issue_book(self.name, self.student_id, book_title, days)
                    self.issued_books_list.append(book_item)

    def return_book(self, isbn):
        for book_item in self.issued_books_list:
            if book_item.isbn == isbn:
                IssueReturn.return_book(book_item)
                self.issued_books_list.remove(book_item)


class Librarian(User):
    def __init__(self, name, location, age, aadhar_id, employee_id):
        super().__init__(name, location, age, aadhar_id)
        self.employee_id = employee_id

    def __repr__(self):
        return self.name + " " + self.location + " " + self.employee_id

    def addBook(self, title, author, publication_date):
        Catalog.add_book(title, author, publication_date)

    def addBookItem(self, title, isbn, rack):
        Catalog.add_book_item(title, isbn, rack)

    def removeBook(self, book):
        Catalog.remove_book(book)

    def removeBookItem(self, bookitem):
        Catalog.remove_book_item(bookitem)

    def removeMember(self, name):
        for member in Member.members_list:
            if member.name == name:
                Member.members_list.remove(member)
                print("{} was successfully removed from the library!".format(name))
                break
        else:
            print("No member exists by this name")

    def viewMembers(self):
        for member in Member.members_list:
            print(member)

    def view_issued_books(self):
        Catalog.view_issued_bookitems(self)