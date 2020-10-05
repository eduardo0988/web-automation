import slash

from resources.PO.Locators import Locator
from resources.PO.Pages.home_page import HomePage
from resources.PO.Pages.login_page import LoginPage
from resources.PO.Pages.logout_page import LogoutPage
from resources.PO.Pages.shopping_cart_page import ShoppingCartPage
from resources.PO.TestData import TestData
from resources.testbase.base_test import BaseTest


class ShoppingCartNavigation(BaseTest):
    """
    Class wich contains test steps to validate that the user is able to navigate to Shopping cart page.
    """
    def test_valid_login(self):
        """
        Test to validate the access to shopping cart page
        """
        driver = self.driver
        try:
            login = LoginPage(driver)
            # login with standard_user
            login.enter_username()
            login.enter_password()
            login.click_login()
            assert self.driver.find_element_by_id(Locator.menu_button).is_displayed()
            assert self.driver.find_element_by_class_name(Locator.product_label).is_displayed()
            login.scroll_page()

            # select a the Backpack and add it to the shopping cart then check that that information is displayed
            home = HomePage(driver)
            home.add_backpack()

            # go to shopping cart
            home = HomePage(driver)
            home.click_cart_button()
            cart = ShoppingCartPage(driver)
            assert cart.find_cart_title().is_displayed()

            # remove item from cart
            cart = ShoppingCartPage(driver)
            cart.remove_item_one()
            if not self.driver.find_element_by_xpath(Locator.cart_qty).is_displayed():
                slash.logger.info("Cart is empty")

            # logout
            logout = LogoutPage(driver)
            logout.click_burger_button()
            logout.click_logout()
            assert login.bot_image
            slash.logger.info("Sucessfully logged out from {}".format(TestData.BASE_URL))
        except Exception as exc:
            slash.add_failure("{}".format(exc))
