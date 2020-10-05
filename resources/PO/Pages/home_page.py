from selenium.webdriver.common.by import By

from time import sleep

from resources.PO.Locators import Locator
from resources.PO.TestData import TestData


class HomePage():
    """
    Class wich contains the locators for Home Page objects
    """
    def __init__(self, driver):
        self.driver = driver
        # home page locators defining
        self.cart_button = driver.find_element(By.XPATH, Locator.cart_button)
        self.back_pack_item = driver.find_element(By.XPATH, Locator.back_pack)

    def click_cart_button(self):
        """
        Method to locate and click the cart button
        """
        self.cart_button.click()
        return self.cart_button

    def add_backpack(self):
        """
        Method to locate the Sauce Labs Backpack and add it to the cart
        """
        self.back_pack_item.click()
        return self.back_pack_item

    def remove_backpack(self):
        """
        Method to remove the backpack from HomePage without using the cart
        """
        self.remove_item = self.driver.find_element_by_xpath(Locator.remove_backpack)
        self.remove_item.click()
        sleep(TestData.DELAY)
        return self.remove_item
