import slash

from resources.PO.Locators import Locator
from resources.PO.Pages.login_page import LoginPage
from resources.PO.Pages.logout_page import LogoutPage
from resources.PO.TestData import TestData
from resources.testbase.base_test import BaseTest


class LogoutTest(BaseTest):  # pylint: disable=too-few-public-methods
    """
    Class wich contains test steps to validate the logout from products page
    """
    def test_valid_logput(self):
        """
        Test to validate logout
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
            logout = LogoutPage(driver)
            logout.click_burger_button()
            logout.click_logout()
            assert login.bot_image
            slash.logger.info("Sucessfully logged out from {}".format(TestData.BASE_URL))
        except Exception as exc:
            slash.add_failure("{}".format(exc))
