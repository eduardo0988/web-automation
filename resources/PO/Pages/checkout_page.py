from selenium.webdriver.common.by import By
from time import sleep

from resources.PO.Locators import Locator
from resources.PO.TestData import TestData


class CheckoutPage():
    """
    Class wich contains the locators and methods for Shopping Cart objects
    """
    def __init__(self, driver):
        self.driver = driver
        # checkout page locators defining
        self.user_info_title = driver.find_element(By.XPATH, Locator.user_info_title)
        self.continue_button = driver.find_element(By.XPATH, Locator.continue_button)
        self.cancel_button = driver.find_element(By.XPATH, Locator.cancel_button)
        self.first_name_field = driver.find_element(By.XPATH, Locator.first_name)
        self.last_name_field = driver.find_element(By.XPATH, Locator.last_name)
        self.zip_code_field = driver.find_element(By.XPATH, Locator.zip_code)

    def locate_user_info_title(self):
        """
        Method to locate the Checkout: Your Information title in checkout page
        """
        return self.user_info_title

    def click_continue_button(self):
        """
        Method to locate and click the continue button
        """
        self.continue_button.click()
        return self.continue_button

    def click_cancel_button(self):
        """
        Metod to locate an click the cancel button
        """
        self.cancel_button.click()
        sleep(TestData.DELAY)
        return self.cancel_button

    def incomplete_user_info(self):
        """
        Method to locate and send the corresponding user information to first name and zip code
        fields (incomplete user info) in Checkout page.
        """
        info = [(self.first_name_field, TestData.FIRST_NAME), (self.zip_code_field, TestData.ZIP_CODE)]
        for item in info:
            field, data = item
            field.clear()
            field.click()
            field.send_keys(data)
            sleep(TestData.DELAY)

    def complete_user_info(self):
        """
        Method to locate and send the corresponding user information to first name, last name and zip code
        fields (complete user info) in Checkout page.
        """
        user_info = [(self.first_name_field, TestData.FIRST_NAME), (self.last_name_field, TestData.LAST_NAME),
                     (self.zip_code_field, TestData.ZIP_CODE)]
        for field in user_info:
            location, name = field
            location.clear()
            location.click()
            location.send_keys(name)
            sleep(TestData.DELAY)
