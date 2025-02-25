import time

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
        continue_btn = self.driver.find_element(By.XPATH, "//span[normalize-space()='CONTINUE']")
        continue_btn.click()

        time.sleep(20)

    def enter_otp(self, otp):
        otp_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "//input[@maxlength='10' and @autocomplete='off' and @type='text' and contains(@class, 'r4vIwl') and contains(@class, 'Ir-g+f')]"))
        )
        otp_field.send_keys(otp)

    def click_login(self):
        login_btn = self.driver.find_element(By.XPATH, "(//button[@type='submit'])[1]")
        login_btn.click()

    def select_address(self):
        dlr_btn = self.driver.find_element(By.XPATH, "//div[@class='lloqNF']//div[2]//div[1]//h3[1]")
        dlr_btn.click()

        deliver_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Deliver Here']"))
        )
        deliver_btn.click()

    def proceed_to_payment(self):
        payment_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='CONTINUE']"))
        )
        payment_btn.click()
        act_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Accept & Continue']"))
        )
        act_button.click()
        time.sleep(15)

    def select_cvv(self):
        cvv = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='cvv']"))
        )
        cvv.send_keys("939")
        cvv_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Continue']"))
        )
        cvv_button.click()


