import pytest
import sys
import os
from utils.driver_factory import get_driver
from utils.data_loader import get_test_data
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture(scope="function")
def setup():
    driver = get_driver()
    driver.get("https://www.flipkart.com/")
    yield driver
    driver.quit()


def test_flipkart_checkout(setup):
    driver = setup
    test_data = get_test_data()

    login_page = LoginPage(driver)
    product_page = ProductPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.close_login_popup()

    product_page.search_product(test_data["search_product"])
    product_page.select_first_product()
    product_page.add_to_cart()

    checkout_page.proceed_to_checkout()
    checkout_page.enter_email("sachan.manas483@gmail.com")
    checkout_page.click_continue()
