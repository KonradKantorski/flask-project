from application import db


# No need for extra personal details as not a business

# since some not nullable below may need to add an if not statement for completeness 

class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key = True)
    book_title = db.Column(db.String(40), nullable=False)
    book_author = db.Column(db.String(30))
    book_length = db.Column(db.Integer, nullable=False)
    book_desc = db.Column(db.String(100))
    year_published = db.Column(db.Integer, nullable=False)
    read_by = db.Column(db.Integer, db.ForeignKey('reader.rid'))
    def __str__(self):
        return f"{self.book_title}, written by {self.book_author}. Description: {self.book_desc}. It is {self.book_length} pages long and was published in {self.year_published}."



class Reader(db.Model): 
    rid = db.Column(db.Integer, primary_key=True)
    forename = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    books = db.relationship('Book', backref='reader')
    def __str__(self):
        return f"{self.forename} {self.surname} "

