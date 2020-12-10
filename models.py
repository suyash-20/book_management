class Book(object):
    def __init__(self, id, name, author_id, year_of_publication):
        self.id = id
        self.name = name
        self.author_id = author_id
        self.year_of_publication = year_of_publication


class Author(object):
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name


class Review(object):
    def __init__(self, id, book_id, rating, review):
        self.id = id
        self.book_id = book_id
        self.rating = rating
        self.review = review