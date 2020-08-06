# -*- coding: utf-8 -*-
# from Book import Book


from User import Member, Librarian


lib = Librarian("Awantik", "bangalore", 30, "asljkl22", "zeke1011")
print(lib)
lib.addBook("shoe dog", "phil knight", "2015")
lib.addBookItem("shoe dog", "123hg", "h1B1")
lib.addBookItem("shoe dog", "124hg", "h1B2")
lib.addBook("Moonwalking with Einstien", "J Foer ", "2017")
lib.addBookItem("Moonwalking with Einstien", "463hg", "C1h1")
lib.addBookItem("Moonwalking with Einstien", "465hg", "C1h2")
lib.addBook("Programming In Python", "Pooja Sharma", "2019")
lib.addBookItem("Programming In Python", "217ab", "d1j1")
lib.addBookItem("Programming In Python", "219ab", "d1j2")
lib.addBookItem("Programming In Python", "221ab", "d1j3")
lib.viewBooks()
lib.removeBookItem("217ab")
lib.viewBooks()
lib.removeBook("shoe dog")
lib.viewBooks()


m1 = Member("Vish", "Bangalore", 23, "Aslijklj22", "std1233")
m2 = Member("Akanksha", "Bangalore", 30, "Dalihjk43", "std1234")

print(m1)
print(m2)

m1.viewBooks()
m1.search_by_book_name("Moonwalking with Einstien")

m1.search_by_author_name("Pooja Sharma")
m1.search_by_author_name("JK rowling")
m1.issue_book("Moonwalking with Einstien", 8)
m2.issue_book("Programming In Python", 10)
m1.viewBooks()

lib.view_issued_books()

m1.return_book("463hg")
m1.viewBooks()
m2.issue_book("shoe dog")

lib.viewMembers()

lib.view_issued_books()