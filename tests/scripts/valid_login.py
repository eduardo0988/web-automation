import slash

from selenium.webdriver.common.keys import Keys
from time import sleep

from resources.PO.TestData import TestData
from resources.testbase.base_test import BaseTest
from resources.PO.Locators import Locator


class ValidLogin(BaseTest):
    """
    Class wich contains test steps to validate a Valid Login Operation
    """
    def test_valid_login(self):
        """
        Test to validate Login with a valid user
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

        except Exception as exc:
            slash.add_failure("{}".format(exc))
