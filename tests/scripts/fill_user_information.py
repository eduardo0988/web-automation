import slash

from resources.PO.Locators import Locator
from resources.PO.Pages.checkout_page import CheckoutPage
from resources.PO.Pages.home_page import HomePage
from resources.PO.Pages.login_page import LoginPage
from resources.PO.Pages.logout_page import LogoutPage
from resources.PO.Pages.overview_page import OverviewPage
from resources.PO.Pages.shopping_cart_page import ShoppingCartPage
from resources.PO.TestData import TestData
from resources.testbase.base_test import BaseTest


class FillInfoTest(BaseTest):
    """
    Class wich contains test steps to validate the user information page
    """
    def test_fill_users_info(self):
        """
        Test to validate the user info page
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

            # go to shopping cart and click checkout button
            home.click_cart_button()
            cart = ShoppingCartPage(driver)
            assert cart.find_cart_title().is_displayed()
            cart.click_checkout_button()

            # go to checkout page
            checkout = CheckoutPage(driver)
            assert checkout.locate_user_info_title().is_displayed()

            # go to checkout page and fill user's info then press continue button
            checkout.complete_user_info()
            checkout.click_continue_button()

            # go to overview page and check that title and payment info are displayed
            over = OverviewPage(driver)
            assert over.locate_overview_title().is_displayed()
            assert over.locate_payment_info().is_displayed()

            over.click_overview_cancel()

            # remove item from inventory page
            home = HomePage(driver)
            home.remove_backpack()

            # logout
            logout = LogoutPage(driver)
            logout.click_burger_button()
            logout.click_logout()
            assert login.bot_image
            slash.logger.info("Sucessfully logged out from {}".format(TestData.BASE_URL))

        except Exception as exc:
            slash.add_failure("{}".format(exc))
