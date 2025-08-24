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

        # Phone number flow
        rp.click_phone_number_button()
        rp.set_add_phone_number()
        rp.click_on_submit_button()
        rp.set_phone_code_field()
        rp.click_on_confirm_button()

        # Payment method flow
        rp.click_on_payment_method()
        rp.click_cc_button()
        rp.set_cc_number()
        rp.set_cvv_code()
        rp.click_cc_add_form()
        rp.click_cc_submit_button()
        rp.click_close_pay_method_button()

        # Message driver and extras
        rp.set_message_on_field()
        rp.click_on_blanket_toggle_button()
        rp.click_max_ice_cream_counter()

        # Request trip
        rp.click_on_order_cab_button()

        #Validate trip details
        driver_name=rp.get_driver_name()
        assert driver_name != ""
        rp.click_on_order_details_button()
        pickup = rp.get_pickup_location_details()
        assert pickup != ""

        destination = rp.get_destination_location_details()
        assert destination != ""

        payment_info = rp.get_payment_method_details()
        assert payment_info == "Tarjeta"

        price = rp.get_trip_price_details()
        assert "Precio" in price



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()