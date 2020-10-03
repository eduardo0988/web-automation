import slash

from selenium.webdriver.common.keys import Keys
from time import sleep

from resources.PO.TestData import TestData
from resources.testbase.base_test import BaseTest
from resources.PO.Locators import Locator


class CompletePurchase(BaseTest):
    """
    Class wich contains test steps to validate a complete purchase.
    """
    def test_purchase(self):
        """
        Test to validate the complete purchase operation
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

            # select a the Backpack and add it to the shopping cart then check that that information is displayed
            self.driver.find_element_by_xpath(Locator.back_pack).click()

            # go to shopping cart
            cart = self.driver.find_element_by_xpath(Locator.cart_button)
            cart.click()
            assert self.driver.find_element_by_xpath(Locator.cart_title).is_displayed()
            assert self.driver.find_element_by_xpath(Locator.cart_qty).is_displayed()
            checkout = self.driver.find_element_by_xpath(Locator.checkout_button)
            assert checkout.is_displayed()
            checkout.click()
            assert self.driver.find_element_by_xpath(Locator.user_info_title).is_displayed()
            sleep(TestData.DELAY)

            # go to checkout page and fill user's info
            info = [(Locator.first_name, TestData.FIRST_NAME), (Locator.last_name, TestData.LAST_NAME),
                    (Locator.zip_code, TestData.ZIP_CODE)]

            for field in info:
                location, data = field
                locate_field = self.driver.find_element_by_xpath(location)
                locate_field.clear()
                locate_field.click()
                locate_field.send_keys(data)
                sleep(TestData.DELAY)

            continue_button = self.driver.find_element_by_xpath(Locator.continue_button)
            continue_button.click()

            assert self.driver.find_element_by_xpath(Locator.overview_title).is_displayed()
            assert self.driver.find_element_by_xpath(Locator.payment_info).is_displayed()

            complete_purchase = self.driver.find_element_by_xpath(Locator.overview_finish_button)
            complete_purchase.click()

            assert self.driver.find_element_by_xpath(Locator.pony_express_image).is_displayed()

        except Exception as exc:
            slash.add_failure("{}".format(exc))
