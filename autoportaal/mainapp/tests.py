from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ViewCommentsCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(ViewCommentsCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(ViewCommentsCase, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/foorumid/')
        #find the form element

        #submit = selenium.find_element_by_name('register')

        #Fill the form with data
        
        # first_name.send_keys('Yusuf')
        # last_name.send_keys('Unary')
        # username.send_keys('unary')
        # email.send_keys('yusuf@qawba.com')
        # password1.send_keys('123456')
        # password2.send_keys('123456')

        #submitting the form
        #submit.send_keys(Keys.RETURN)

        #check the returned result
        assert 'Teema pealkiri' in selenium.page_source