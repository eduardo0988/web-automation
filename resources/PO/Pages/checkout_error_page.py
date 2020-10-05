from selenium.webdriver.common.by import By

from resources.PO.Locators import Locator


class CheckoutErrorPage():
    """
    Class wich contains the locators and methods for Error objects in checkout page
    """
    def __init__(self, driver):
        self.driver = driver
        # shopping cart page locators defining
        self.error_message = driver.find_element(By.XPATH, Locator.error_message)

    def check_last_name_error(self):
        """
        Method to checks if the Missing Last Name error message is displayed
        """
        return self.error_message
