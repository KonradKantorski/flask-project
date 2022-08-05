#from flask_testing import LiveServerTestCase
#from selenium import webdriver
#from urllib.request import urlopen
#from flask import url_for
#from application import app, db
#from application.models import *
#from application.forms import *


# below does not work, gives error for xpath of the submit button -- I have tried changing the xpath but it is still not picking it up. More info in READ.ME


#class TestBase(LiveServerTestCase):
#    TEST_PORT = 5050

#    def create_app(self):
#        app.config.update(
#            SQLALCHEMY_DATABASE_URI = 'sqlite:///test-app.db',
#            LIVESERVER_PORT = self.TEST_PORT,
#            DEBUG = True,
#            TESTING = True
#
#        )
#
#        return app 

#    def setUp(self):
#        db.create_all()
#        options = webdriver.chrome.options.Options()
#        options.add_argument('--headless')
#        self.driver = webdriver.Chrome(options=options)
#        self.driver.get(f'http://localhost:{self.TEST_PORT}/add-book')


#    def tearDown(self):
#        self.driver.quit()
#        db.session.remove()
#        db.drop_all()
 


#class TestAddBook(TestBase):
#    def submit_input(self, test_case):
#        book_title_field = self.driver.find_element_by_xpath('/html/body/div/form/input[2]')
#        book_author_field = self.driver.find_element_by_xpath('/html/body/div/form/input[3]')
#        book_length_field = self.driver.find_element_by_xpath('/html/body/div/form/input[4]')
#        book_desc_field = self.driver.find_element_by_xpath('/html/body/div/form/textarea')
#        public_year_field = self.driver.find_element_by_xpath('/html/body/div/form/input[5]')
#        submit = self.driver.find_element_by_xpath('/html/body/div/form/input[7]')
#        book_title_field.send_keys(test_case[0])
#        book_author_field.send_keys(test_case[1])
#        book_length_field.send_keys(test_case[2])
#        book_desc_field.send_keys(test_case[3])
#        public_year_field.send_keys(test_case[4])
#        submit.click()
#
#    def test_add_book(self):
#        test_case = "Title", "Anon", 356, "Brief description", 2000
#        self.submit_input(test_case)
#        assert list(Book.query.all()) != []
#        assert Book.query.filter_by(book_title="Title").first() is not None


