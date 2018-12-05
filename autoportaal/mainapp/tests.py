from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
chromeDriver = BASE_DIR +  "/mainapp/chromeDriver/chromedriver.exe"

class AllTests(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome(chromeDriver)
        super(AllTests, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AllTests, self).tearDown()


    def test_view_forum(self):
        selenium = self.selenium
        #Avame lehe, mida tahame testida
        selenium.get('https://auto25.tk/foorumid')
        # Kontrollim kas saime kätte
        assert 'Teema pealkiri'  in selenium.page_source

        #Otsime element nimega pealkiri
        pealkiri_link = selenium.find_element_by_link_text('pealkiri')
        pealkiri_link.click()
        assert '3123123'  in selenium.page_source



    # Ei saanud Goolge login tööle, seega kommenteerisin selle hektel välja      
    #                       ||
    #                       ˇˇ
    # def test_google_login (self):
    #     driver = self.selenium
    #     mail_address = 'Sinu meili aadress'
    #     password = 'parool'

    #     url = 'https://www.google.com/accounts/Login?hl=ja&continue=http://www.google.co.jp/'
    #     driver.get(url)

    #     driver.find_element_by_id("identifierId").send_keys(mail_address)
    #     driver.find_element_by_id("identifierNext").click()
    #     driver.find_element_by_name("password").send_keys(password)
    #     element = driver.find_element_by_id('passwordNext')
    #     driver.execute_script("arguments[0].click();", element)


    def test_search(self):
        selenium = self.selenium
        
        selenium.get('https://auto25.tk')
        assert 'Find yourself a suitable vehicle'  in selenium.page_source
        
        selenium.find_element_by_css_selector(".form-control.mainsearch").send_keys("Opel Astra")
        selenium.find_element_by_css_selector(".btn.btn-primary.searchbutton").click()
        new_url = selenium.current_url
        assert "https://auto25.tk/?" in new_url