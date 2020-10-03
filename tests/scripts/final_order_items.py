import slash

from selenium.webdriver.common.keys import Keys
from time import sleep

from resources.PO.TestData import TestData
from resources.testbase.base_test import BaseTest
from resources.PO.Locators import Locator


class FinalOrder(BaseTest):
    """
    Class wich contains test steps to validate that selected items in overview page are the same in the cart page
    """
    def test_single_item(self):
        """
        Test to validate that the selected items in overview page remains in checkout page
        """
        try:
            # login with standard_user
            self.locate_user_login.send_keys(TestData.USERS[0])
            locate_user_password = self.driver.find_element_by_id(Locator.login_password)
            locate_user_password.clear()
            locate_user_password.click()
            locate_user_password.send_keys(TestData.PASSWORD)
            sleep(TestData.DELAY)
            locate_login_button = self.driver.find_element_by_id(Locator.login_button)
            locate_login_button.click()
            assert self.driver.find_element_by_id(Locator.menu_button).is_displayed()

            # scroll down the page then up back to the top
            scroll_down = self.driver.find_element_by_tag_name("html")
            scroll_down.send_keys(Keys.END)
            sleep(TestData.DELAY)
            scroll_down.send_keys(Keys.CONTROL + Keys.HOME)
            sleep(TestData.DELAY)

            # Add Backpack, Bike Light and Red T-shirt items to the shopping cart
            # then check that that information is displayed
            items_to_add = [Locator.back_pack, Locator.bike_light, Locator.red_tshirt]
            for item in items_to_add:
                self.driver.find_element_by_xpath(item).click()
                sleep(TestData.DELAY)

            # go to shopping cart
            cart = self.driver.find_element_by_xpath(Locator.cart_button)
            cart.click()
            assert self.driver.find_element_by_xpath(Locator.cart_title).is_displayed()
            assert self.driver.find_element_by_xpath(Locator.cart_qty).is_displayed()

            # find added elements (Backpack, Bike Light and Red T-shirt) by id
            products = [Locator.back_pack_id, Locator.bike_light_id, Locator.red_tshirt_id]
            for product in products:
                element = self.driver.find_element_by_id(product)
                assert element.is_displayed()
                sleep(TestData.DELAY)

            # remove items from cart
            items_to_remove = [Locator.remove_third_element, Locator.remove_second_element,
                               Locator.remove_first_element]

            for stuff in items_to_remove:
                remove_item = self.driver.find_element_by_xpath(stuff)
                remove_item.click()
                sleep(TestData.DELAY)
            if not self.driver.find_element_by_xpath(Locator.cart_qty).is_displayed():
                slash.logger.info("Cart is empty")

        except Exception as exc:
            slash.add_failure("{}".format(exc))
