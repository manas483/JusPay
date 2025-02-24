from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    """Initialize and return a Chrome WebDriver instance."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")

    # FIX: Pass options correctly without explicit driver path
    driver = webdriver.Chrome(service=webdriver.ChromeService(ChromeDriverManager().install()), options=options)
    return driver
