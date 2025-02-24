from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(service=webdriver.ChromeService(ChromeDriverManager().install()), options=options)
    return driver
