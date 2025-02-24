import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def search_product(self, products):
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys(products + Keys.RETURN)

    def select_first_product(self):
        self.driver.implicitly_wait(5)
        products = self.driver.find_elements(By.CLASS_NAME, "KzDlHZ")
        if products:
            products[4].click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(5)
            
    def add_to_cart(self):
        add_to_cart_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]")
        add_to_cart_button.click()
