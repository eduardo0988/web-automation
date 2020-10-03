import datetime
import slash


from time import sleep

from resources.PO.Locators import Locator
from resources.PO.TestData import TestData
from resources.testbase.base_test import BaseTest


class InvalidLogin(BaseTest):
    """
    Class wich contains test steps to validate a Invalid Login Operation.
    """
    def test_invalid_login(self):
        """
        Test to validate Login with an invalid user
        """
        try:
            self.locate_user_login.send_keys(TestData.INVALID_USER)
            locate_user_password = self.driver.find_element_by_id(Locator.login_password)
            locate_user_password.clear()
            locate_user_password.click()
            locate_user_password.send_keys(TestData.PASSWORD)
            sleep(TestData.DELAY)
            locate_login_button = self.driver.find_element_by_id(Locator.login_button)
            locate_login_button.click()
            assert self.driver.find_element_by_xpath(Locator.error_icon)
            slash.logger.info("Invalid user, please try again")
            self.locate_user_login.clear()
            locate_user_password.clear()
            sleep(TestData.DELAY)

        except Exception as exc:
            slash.add_failure("{}".format(exc))

    def after(self):
        """
        Override after from BaseTest to close the browser instance
        """
        if self.driver is not None:
            slash.logger.info("-"*80)
            slash.logger.info("Test Environment Destroyed")
            slash.logger.info("Run Completed at:{}".format(datetime.datetime.now()))
            self.driver.close()
            self.driver.quit()
