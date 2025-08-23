from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import data.data
from utils.retrieve_code import retrieve_phone_code

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    taxi_button = (By.XPATH, '//button[@class="button round" and text()="Pedir un taxi"]')
    comfort_tariff_card = (By.CSS_SELECTOR, ".tariff-cards .tcard:nth-child(5)")
    phone_number_button = (By.CLASS_NAME, "np-button")
    add_phone_number = (By.ID, 'phone')
    submit_phone_button = (By.XPATH, '//button[@class="button full" and text()="Siguiente"]')
    phone_code_field = (By.ID, "code")
    confirm_button = (By.XPATH, '//button[@class="button full" and text()="Confirmar"]')
    payment_method = (By.CLASS_NAME, "pp-button.filled")
    cc_field_button = (By.XPATH, "//div[@class='pp-title' and text()='Agregar tarjeta']")
    add_cc_number = (By.ID, 'number')
    cvv_code_field = (By.XPATH, "//input[@id='code' and @placeholder='12']")
    cc_add_form = (By.CSS_SELECTOR, "div.card-wrapper")
    cc_submit_button = (By.XPATH, "//button[@type='submit' and text()='Agregar']")
    close_pay_method = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')
    message_field = (By.ID, 'comment')
    blanket_toggle_button = (By.XPATH, "//div[@class='r-sw-label' and text()='Manta y pañuelos']/following::span[@class='slider round'][1]")
    ice_cream_counter = (By.XPATH, "//div[@class='r-counter-label' and text()='Helado']/following::div[contains(@class,'counter-plus')][1]")
    order_cab_button = (By.XPATH, '//button[@class="smart-button"]/span[@class="smart-button-main" and text()="Pedir un taxi"]')
    driver_name_field = (By.XPATH, "//div[@class='order-btn-group']/div[2]")
    order_details_button = (By.XPATH, "//div[text()='Detalles']/preceding-sibling::button")
    pickup_location = (By.XPATH, "//div[@class='order-details-content']/div[@class='o-d-h' and following-sibling::div[text()='Lugar de recogida']]")
    destination_location = (By.XPATH, "//div[@class='order-details-content']/div[@class='o-d-h' and following-sibling::div[text()='Dirección de destino']]")
    payment_method_details = (By.XPATH, "//div[@class='order-details-content']/div[@class='o-d-h' and following-sibling::div[text()='Método de pago']]")
    trip_price = (By.XPATH, "//div[@class='order-details-content']/div[@class='o-d-sh' and contains(text(),'Precio')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,5)
        self.wait_ride = WebDriverWait(driver,40)

    def set_from(self, from_address):
        self.wait.until(EC.presence_of_element_located(self.from_field)).send_keys(from_address)

    def set_to(self, to_address):
        self.wait.until(EC.presence_of_element_located(self.to_field)).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_taxi_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.taxi_button))

    def click_on_taxi_button(self):
        self.get_taxi_button().click()

    def get_comfort_option_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.comfort_tariff_card))

    def click_comfort_option_button(self):
        self.get_comfort_option_button().click()

    def get_phone_number_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.phone_number_button))

    def click_phone_number_button(self):
        self.get_phone_number_button().click()

    def set_add_phone_number(self, phone_number=None):
        if phone_number is None:
            phone_number = data.data.phone_number
        self.wait.until(EC.presence_of_element_located(self.add_phone_number)).send_keys(phone_number)

    def get_phone_number(self):
        return self.driver.find_element(*self.add_phone_number).get_property('value')

    def get_submit_phone_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.submit_phone_button))

    def click_on_submit_button(self):
        self.get_submit_phone_button().click()

    def set_phone_code_field(self):
        phone_code = retrieve_phone_code(self.driver)
        self.wait.until(EC.presence_of_element_located(self.phone_code_field)).send_keys(phone_code)

    def get_confirm_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.confirm_button))

    def click_on_confirm_button(self):
        self.get_confirm_button().click()

    def get_payment_method(self):
        return self.wait.until(EC.element_to_be_clickable(self.payment_method))

    def click_on_payment_method(self):
        self.get_payment_method().click()

    def get_cc_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.cc_field_button))

    def click_cc_button(self):
        self.get_cc_button().click()

    def get_cc_input_field(self):
        return self.wait.until(EC.visibility_of_element_located(self.add_cc_number))

    def set_cc_number(self, card_number=None):
        if card_number is None:
            card_number = data.data.card_number
        self.wait.until(EC.presence_of_element_located(self.add_cc_number)).send_keys(card_number)

    def get_cc_number(self):
        return self.driver.find_element(*self.add_cc_number).get_property('value')

    def get_cvv_code_field(self):
        return self.wait.until(EC.visibility_of_element_located(self.cvv_code_field))

    def set_cvv_code(self, card_code=None):
        if card_code is None:
            card_code = data.data.card_code
        self.wait.until(EC.element_to_be_clickable(self.cvv_code_field)).send_keys(card_code)

    def get_cc_add_form(self):
        return self.wait.until(EC.visibility_of_element_located(self.cc_add_form))

    def click_cc_add_form(self):
        self.get_cc_add_form().click()

    def get_cvv_code(self):
        return self.driver.find_element(*self.cvv_code_field).get_property('value')

    def get_cc_submit_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.cc_submit_button))

    def click_cc_submit_button(self):
        self.get_cc_submit_button().click()

    def get_close_pay_method_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.close_pay_method))

    def click_close_pay_method_button(self):
        self.get_close_pay_method_button().click()

    def get_message_field(self):
        return self.wait.until(EC.presence_of_element_located(self.message_field))

    def set_message_on_field(self, message_for_driver = None ):
        if message_for_driver is None:
         message_for_driver = data.data.message_for_driver
        self.wait.until(EC.presence_of_element_located(self.message_field)).send_keys(message_for_driver)

    def get_message_on_field(self):
        return self.driver.find_element(*self.message_field).get_property('value')

    def get_blanket_toggle_button(self):
        return self.wait.until(EC.visibility_of_element_located(self.blanket_toggle_button))

    def click_on_blanket_toggle_button(self):
        self.get_blanket_toggle_button().click()

    def get_ice_cream_counter(self):
        return self.wait.until(EC.element_to_be_clickable(self.ice_cream_counter))

    def click_max_ice_cream_counter(self):
        self.get_ice_cream_counter().click()
        self.get_ice_cream_counter().click()

    def get_order_cab_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.order_cab_button))

    def click_on_order_cab_button(self):
        self.get_order_cab_button().click()

    def get_driver_name_field(self):
        return self.wait_ride.until(EC.presence_of_element_located(self.driver_name_field))

    def get_driver_name(self):
        return self.get_driver_name_field().text

    def get_order_details_button(self):
        return self.wait_ride.until(EC.element_to_be_clickable(self.order_details_button))

    def click_on_order_details_button(self):
        self.get_order_details_button().click()

    def get_pickup_location_element(self):
        return self.wait.until(EC.presence_of_element_located(self.pickup_location))

    def get_pickup_location_details(self):
        return self.get_pickup_location_element().text

    def get_destination_location_element(self):
        return self.wait.until(EC.presence_of_element_located(self.destination_location))

    def get_destination_location_details(self):
        return self.get_destination_location_element().text

    def get_payment_method_element(self):
        return self.wait.until(EC.presence_of_element_located(self.payment_method_details))

    def get_payment_method_details(self):
        return self.get_payment_method_element().text

    def get_trip_price_element(self):
        return self.wait.until(EC.presence_of_element_located(self.trip_price))

    def get_trip_price_details(self):
        return self.get_trip_price_element().text





























