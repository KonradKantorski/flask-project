from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for
from application import app, db
from application.models import *
from application.forms import *

class TestBase(LiveServerTestCase):
    TEST_PORT = 5050

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test-app.db',
            LIVESERVER_PORT = self.TEST_PORT,
            DEBUG = True,
            TESTING = True

        )

        return app 

    def setUp(self):
        db.create_all()
        options = webdriver.chrome.options.Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(f'http://localhost:{self.TEST_PORT}/add-reader')


    def tearDown(self):
        self.driver.quit()
        db.session.remove()
        db.drop_all()
 
# will xpaths always work since they are inconsistent, or do we sometimes change them?

class TestAddReader(TestBase):
    def submit_input(self, test_case):
        forename_field = self.driver.find_element_by_xpath('/html/body/div/form/input[1]')
        surname_field = self.driver.find_element_by_xpath('/html/body/div/form/input[2]')
        submit = self.driver.find_element_by_xpath('/html/body/div/form/input[3]')
        forename_field.send_keys(test_case[0])
        surname_field.send_keys(test_case[1])
        submit.click()

    def test_add_reader(self):
        test_case = "Jane", "Doe"
        self.submit_input(test_case)
        assert list(Reader.query.all()) != []
        assert Reader.query.filter_by(forename="Jane").first() is not None


