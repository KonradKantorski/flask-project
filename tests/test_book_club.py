from flask import url_for
from application import app, db
from application.models import *
from flask_testing import TestCase

from application.routes import *

# ----------------------------------------------------------------- GET Reuquest tests

# test in different database so that we do not risk production database

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test-app.db',
            WTF_CSRF_ENABLED = False,
            DEBUG = True,
            SECRET_KEY = 'DMNSFJDNFS'
        )
        return app

    def setUp(self):   # runs before every single test with data
        db.create_all()
        book1 = Book(book_title = 'Sample Book', book_author = 'Test Smith', book_length = 250, book_desc = 'Sample description', year_published = 1984)
        reader1 = Reader(forename = 'Sample', surname = 'Reader')
        db.session.add(book1)
        db.session.add(reader1)
        db.session.commit()

    def tearDown(self): # runs after every test to clean up and close any active db session
        db.session.remove()
        db.drop_all()

#test home page

class TestHomeView(TestBase):
    def test_get_home(self):
        response = self.client.get(url_for('index'))
        self.assert200(response)
        self.assertIn(b'Welcome to the Book Club', response.data)
#test add reader 

    def test_get_new_reader(self):
        response = self.client.get(url_for('create_reader'))
        self.assert200(response)
        self.assertIn(b'Enter Forename', response.data)

#test view-all-readers

    def test_view_readers(self):
        response = self.client.get(url_for('view_all_readers'))
        self.assert200(response)
        self.assertIn(b'Readers', response.data)


#test view-readers by id

    def test_view_readers_by_id(self):
        response = self.client.get(url_for('get_reader_by_id', id=1))
        self.assert200(response)
        self.assertIn(b'Reader Page', response.data)

#test update reader
    def test_update_reader(self):
        response = self.client.get(url_for('update_reader', id=1))
        self.assert200(response)
        self.assertIn(b'Enter Forename', response.data)

#test delete reader
    def test_delete_reader(self):
        response = self.client.get(url_for('delete_reader', id=1), follow_redirects = True)
        self.assert200(response)
        self.assertIn(b'Readers', response.data)

#   books add
    def test_add_book(self):
        response = self.client.get(url_for('add_new_book'))
        self.assert200(response)
        self.assertIn(b'Book', response.data)

# books read
    def test_view_books(self):
        response = self.client.get(url_for('view_all_books'))
        self.assert200(response)
        self.assertIn(b'Book List', response.data)

# books update
    def test_update_book(self):
        response = self.client.get(url_for('update_book', id=1))
        self.assert200(response)
        self.assertIn(b'Book Title', response.data)

#  book delete
    def test_delete_book(self):
        response = self.client.get(url_for('delete_book', id=1), follow_redirects = True)
        self.assert200(response)
        self.assertIn(b'Book List', response.data)

# -------------------------------------------------------- POST requests

class TestPostRequests(TestBase):
    def test_post_add_reader(self):
        response = self.client.post(
            url_for('create_reader'),
            data = dict(forename = 'John', surname = 'Snow'), follow_redirects = True
        )

        self.assert200(response)
        self.assertIn(b'John Snow', response.data)
# post reader update
    def test_post_update_reader(self):
        response = self.client.post(
            url_for('update_reader', id=1),
            data = dict(forename='Anna', surname='Jones'), follow_redirects = True

        )
        
        self.assert200(response)
        self.assertIn(b'Anna Jones', response.data)
        assert Reader.query.filter_by(forename='John').first() is None
# post add book
    def test_post_add_book(self):
        response = self.client.post(
            url_for('add_new_book'),
            data = dict(
                book_title = 'The Hobbit',
                book_author = 'J. R. R. Tolkien',
                book_desc = 'Adventures in the shire and beyond',
                book_length = 239,
                year_published = 1937,
                read_by = 1
            ),

                follow_redirects = True
        )

        self.assert200(response)
        self.assertIn(b'Book Club', response.data)
        self.assertIn(b'Book List', response.data)
        self.assertIn(b'The Hobbit', response.data)
        self.assertIn(b'J. R. R. Tolkien', response.data)
        self.assertIn(b'Adventures in the shire and beyond', response.data)
        self.assertIn(b'1937', response.data)


# #post update book
    def test_post_update_book(self):
        response = self.client.post(
            url_for('update_book', id=1),
            data = dict(
                book_title = 'A Feast for Crows',
                book_author = 'George R. R. Martin',
                book_desc = 'Only vultures win',
                book_length = 753,
                year_published = 2005,
                read_by = 1
            ),

                follow_redirects = True
        )
        
        self.assert200(response)
        self.assertIn(b'Book Club', response.data)
        self.assertIn(b'Book List', response.data)
        self.assertIn(b'Only vultures win', response.data)
        self.assertIn(b'published in 2005', response.data)
        
   


#seperate assertIns
