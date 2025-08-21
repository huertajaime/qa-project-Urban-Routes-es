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
        self.routes_page.get_cc_add_form()
        self.routes_page.click_cc_add_form()
        self.routes_page.get_cvv_code()
        self.routes_page.get_cc_submit_button()
        self.routes_page.click_cc_submit_button()
        self.routes_page.get_close_pay_method_button()
        self.routes_page.click_close_pay_method_button()
        self.routes_page.get_message_field()
        self.routes_page.set_message_on_field()
        self.routes_page.get_message_on_field()
        self.routes_page.get_blanket_toggle_button()
        self.routes_page.click_on_blanket_toggle_button()
        self.routes_page.get_ice_cream_counter()
        self.routes_page.click_max_ice_cream_counter()
        self.routes_page.get_order_cab_button()
        self.routes_page.click_on_order_cab_button()

        time.sleep(5)


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()