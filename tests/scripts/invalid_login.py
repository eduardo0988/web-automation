import slash

from resources.PO.Locators import Locator
from resources.PO.Pages.login_page import LoginPage
from resources.PO.Pages.logout_page import LogoutPage
from resources.PO.TestData import TestData
from resources.testbase.base_test import BaseTest


class InvalidLogin(BaseTest):
    """
    Class wich contains test steps to validate a Invalid Login Operation.
    """
    def test_invalid_login(self):
        """
        Test to validate Login with an invalid user, then use a valid user and logout from page
        """
        driver = self.driver
        try:
            login = LoginPage(driver)
            # login with invalid_user
            login.enter_username(TestData.INVALID_USER)
            login.enter_password()
            login.click_login()
            assert self.driver.find_element_by_xpath(Locator.error_icon)
            slash.logger.info("Invalid user, please try again")

            # login with valid_user
            login.enter_username()
            login.enter_password()
            login.click_login()
            assert self.driver.find_element_by_id(Locator.menu_button).is_displayed()
            assert self.driver.find_element_by_class_name(Locator.product_label).is_displayed()
            login.scroll_page()
            logout = LogoutPage(driver)
            logout.click_burger_button()
            logout.click_logout()
            assert login.bot_image
            slash.logger.info("Sucessfully logged out from {}".format(TestData.BASE_URL))
        except Exception as exc:
            slash.add_failure("{}".format(exc))
