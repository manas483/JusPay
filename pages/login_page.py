from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def close_login_popup(self):

        try:
            close_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'✕')]")
            close_button.click()
        except:
            pass

    def login(self, username, password):

        self.driver.find_element(By.XPATH, "//input[@class='_2IX_2- VJZDxU']").send_keys(username)
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
