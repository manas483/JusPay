from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PaymentPage(BasePage):
    NET_BANKING_OPTION = (By.XPATH, "//label[@for='NET_OPTIONS']//div[@class='_9-suWS']")
    UPI_OPTION = (By.XPATH, "//span[normalize-space()='UPI']")
    CARD_OPTION = (By.XPATH, "//span[normalize-space()='Credit / Debit / ATM Card']")
    OTP_FIELD = (By.XPATH, "//input[@type='password']")
    SUBMIT_OTP = (By.XPATH, "//button[contains(text(),'Submit')]")

    def select_payment_method(self, method):
        if method == "netbanking":
            self.click(self.NET_BANKING_OPTION)
        elif method == "upi":
            self.click(self.UPI_OPTION)
        elif method == "card":
            self.click(self.CARD_OPTION)

    def enter_otp(self, otp):
        self.enter_text(self.OTP_FIELD, otp)
        self.click(self.SUBMIT_OTP)
