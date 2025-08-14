from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    taxi_button = (By.XPATH, '//button[@class="button round" and text()="Pedir un taxi"]')
    comfort_tariff_card = (By.CSS_SELECTOR, ".tariff-cards .tcard:nth-child(4)")
    phone_number_button = (By.CLASS_NAME, "np-button")
    add_phone_number = (By.ID, 'phone')
    payment_pp_button = (By.CLASS_NAME, "pp-button filled")



    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,5)

    def set_from(self, from_address):
        #self.driver.find_element(*self.from_field).send_keys(from_address)
        self.wait.until(EC.presence_of_element_located(self.from_field)).send_keys(from_address)

    def set_to(self, to_address):
        #self.driver.find_element(*self.to_field).send_keys(to_address)
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

    def click_phone_number_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.phone_number_button))

    def set_phone_number(self, phone_number):
        self.wait.until(EC.presence_of_element_located(self.add_phone_number)).send_keys(phone_number)

    def get_phone_number(self):
        return self.driver.find_element(*self.add_phone_number).get_property('value')

    def set_new_phone_number(self, add_phone_number):
        self.set_phone_number(add_phone_number)

    def get_payment_pp_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.payment_pp_button))

    def click_on_payment_pp_button(self):
        self.get_payment_pp_button().click()