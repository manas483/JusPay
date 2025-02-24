from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    def proceed_to_checkout(self):
        checkout_btn = self.driver.find_element(By.XPATH, "//button[.//span[contains(text(), 'Place Order')]]")
        checkout_btn.click()

    def enter_email(self, email):
        email_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='text']"))
        )
        email_field.send_keys(email)

    def click_continue(self):
        continue_btn = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        continue_btn.click()

    def enter_otp(self, otp):
        otp_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='text']"))
        )
        otp_field.send_keys(otp)

    def click_login(self):
        login_btn = self.driver.find_element(By.XPATH, "//button[contains(text(),'Login')]")
        login_btn.click()

    def select_address(self):
        address_radio = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='radio']"))
        )
        address_radio.click()

        deliver_btn = self.driver.find_element(By.XPATH, "//button[contains(text(),'Deliver Here')]")
        deliver_btn.click()

    def proceed_to_payment(self):
        payment_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continue to Payment')]"))
        )
        payment_btn.click()

    # def enter_payment_details(self, card_number, cvv):
    #     """Enters payment details (mock)."""
    #     self.driver.find_element(By.NAME, "debitCard").send_keys(card_number)
    #     self.driver.find_element(By.NAME, "cvv").send_keys(cvv)
    #
    # def enter_otp(self, otp):
    #     """Simulates OTP entry."""
    #     self.driver.find_element(By.NAME, "otp").send_keys(otp)
