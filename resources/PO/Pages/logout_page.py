from selenium.webdriver.common.by import By
from time import sleep

from resources.PO.Locators import Locator
from resources.PO.TestData import TestData

class LogoutPage():
    """
    Class wich contains the locators for Logout Page objects
    """
    def __init__(self, driver):
        self.driver = driver
        # logout locators defining
        self.burger_button = driver.find_element(By.CLASS_NAME, Locator.burger_button)
        self.logout_button = driver.find_element(By.ID, Locator.logout_button)
    
    def click_burger_button(self):
        """
        Method to locate and click the burger button
        """
        self.burger_button.click()
        return self.burger_button

    def click_logout(self):
        """
        Method to locate and click the logout button
        """
        self.logout_button.click()
        sleep(TestData.DELAY)
        return self.logout_button
