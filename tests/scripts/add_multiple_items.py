import slash

from time import sleep

from resources.PO.Locators import Locator
from resources.PO.Pages.home_page import HomePage
from resources.PO.Pages.login_page import LoginPage
from resources.PO.Pages.logout_page import LogoutPage
from resources.PO.Pages.shopping_cart_page import ShoppingCartPage
from resources.PO.TestData import TestData
from resources.testbase.base_test import BaseTest


class MultipleItemTest(BaseTest):
    """
    Class wich contains test steps to validate the addition of a multiple items to the shopping cart
    """
    def test_single_item(self):
        """
        Test to validate the addition of a multiple items to the shopping cart
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

            # select a the Backpack, Bike Light and Red T-shirt add them to the shopping cart
            # then check that that information is displayed
            items_to_add = [Locator.back_pack, Locator.bike_light, Locator.red_tshirt]
            for item in items_to_add:
                self.driver.find_element_by_xpath(item).click()
                sleep(TestData.DELAY)

            # go to shopping cart
            home = HomePage(driver)
            home.click_cart_button()
            cart = ShoppingCartPage(driver)
            assert cart.find_cart_title().is_displayed()
            assert cart.get_items_cart_qty().is_displayed()

            # remove item from cart
            items_to_remove = [Locator.remove_third_element, Locator.remove_second_element,
                               Locator.remove_first_element]
            for stuff in items_to_remove:
                remove_item = self.driver.find_element_by_xpath(stuff)
                remove_item.click()
                sleep(TestData.DELAY)
            if not cart.get_items_cart_list().is_displayed():
                slash.logger.info("Cart is empty")

            # logout
            logout = LogoutPage(driver)
            logout.click_burger_button()
            logout.click_logout()
            assert login.bot_image
            slash.logger.info("Sucessfully logged out from {}".format(TestData.BASE_URL))
        except Exception as exc:
            slash.add_failure("{}".format(exc))
