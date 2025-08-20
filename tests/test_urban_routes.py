import time

from data import data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages import urban_routes_page as urp

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability("goog:loggingPrefs", value={'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=chrome_options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = urp.UrbanRoutesPage(cls.driver)


    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = urp.UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to



    def test_set_options(self):
        self.routes_page.click_on_taxi_button()
        self.routes_page.click_comfort_option_button()
        self.routes_page.click_phone_number_button()
        self.routes_page.set_add_phone_number()
        self.routes_page.get_phone_number()
        self.routes_page.click_on_submit_button()
        self.routes_page.set_phone_code_field()
        self.routes_page.click_on_confirm_button()
        self.routes_page.click_on_payment_method()
        self.routes_page.click_cc_button()
        self.routes_page.set_cc_number()
        self.routes_page.get_cc_number()
        self.routes_page.get_cvv_code_field()
        self.routes_page.set_cvv_code()
        self.routes_page.get_cvv_code()
        #self.routes_page.click_on_tab_key()





        time.sleep(5)


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()