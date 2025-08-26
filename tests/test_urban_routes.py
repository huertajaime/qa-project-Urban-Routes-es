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
        rp = self.routes_page
        # Select trip - options
        rp.click_on_taxi_button()
        rp.click_comfort_option_button()
        assert "active" in rp.confirm_comfort_option()

    def test_set_phone_options(self):
        rp = self.routes_page
        # Phone number flow
        rp.click_phone_number_button()
        rp.set_add_phone_number()
        rp.get_submit_phone_button()
        rp.click_on_submit_button()
        rp.set_phone_code_field()
        rp.click_on_confirm_button()
        assert rp.confirm_phone_is_set() !=""



    def test_set_cc_info(self):
        rp = self.routes_page
        # Payment method flow
        rp.get_payment_method()
        rp.click_on_payment_method()
        rp.click_cc_button()
        rp.get_cc_input_field()
        rp.set_cc_number()

        rp.get_cvv_code()
        rp.set_cvv_code()
        rp.click_cc_add_form()
        rp.click_cc_submit_button()
        rp.click_close_pay_method_button()
        assert data.card_number in rp.get_cc_number()

    def test_set_message(self):
        rp = self.routes_page
        # Message driver and extras
        rp.get_message_field()
        rp.set_message_on_field()
        assert data.message_for_driver in rp.get_message_on_field()

    def test_request_blanket(self):
        rp = self.routes_page
        rp.click_on_blanket_toggle_button()
        assert rp.get_blanket_toggle_button()

    def test_request_ice_cream(self):
        rp = self.routes_page
        rp.get_ice_cream_counter()
        rp.click_max_ice_cream_counter()
        assert int(rp.get_counter_ice_cream_element()) == 2

    def test_order_cab(self):
        rp = self.routes_page
        # Request trip
        rp.click_on_order_cab_button()
        rp.get_order_cab_button()
        assert rp.confirm_cab_button_element()

    def test_get_ride_info(self):
        rp = self.routes_page
        #Validate trip details
        rp.get_driver_name_field()
        driver_name=rp.get_driver_name()
        assert driver_name != ""
        rp.click_on_order_details_button()
        pickup = rp.get_pickup_location_details()
        assert pickup != ""

        rp.get_destination_location_element()
        destination = rp.get_destination_location_details()
        assert destination != ""

        rp.get_payment_method_element()
        payment_info = rp.get_payment_method_details()
        assert payment_info == "Tarjeta"

        rp.get_trip_price_element()
        price = rp.get_trip_price_details()
        assert "Precio" in price



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()