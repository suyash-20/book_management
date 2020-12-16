
class Book(object):
    def __init__(self, id, name, author_id, year_of_publication):
        self.id = id
        self.name = name
        self.author_id = author_id
        self.year_of_publication = year_of_publication
    
    def print(self):
        print(self.id,"\t", self.name," \t", self.author_id, " \t", self.year_of_publication)


class Author(object):
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def print(self):
        print(self.id, "\t", self.first_name, " \t", self.last_name)


class Review(object):
    def __init__(self, id, book_name, rating):
        self.id = id
        self.book_name = book_name
        self.rating = rating

    def print(self):
        print(self.id,  "\t", self.book_name,  "\t", self.rating)

#EMURATED VARIABLES FOR USER CHOICE
class MainChoice:
    Books = 1
    Authors = 2
    BookReviews = 3

class BookMenu:
    Browse = 1
    AddTo = 2

class AuthorMenu:
    Browse = 1
    AddTo = 2

class ReviewMenu:
    Browse = 1
    AddTo = 2


def print_messages():
    print("----------Welcome to the book store!----------")
    print("________________________________________________\n")
    
    print("Here's our catalogue to explore around:")
    print("""
    1. Books
    2.Authors
    3.Book Reviews
    """)