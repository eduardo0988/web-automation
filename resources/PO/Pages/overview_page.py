from selenium.webdriver.common.by import By
from time import sleep

from resources.PO.Locators import Locator
from resources.PO.TestData import TestData


class OverviewPage():
    """
    Class wich contains the locators and methods for Overview page objects
    """
    def __init__(self, driver):
        self.driver = driver
        # overview page locators defining
        self.overview_title = driver.find_element(By.XPATH, Locator.overview_title)
        self.payment_info = driver.find_element(By.XPATH, Locator.payment_info)
        self.overview_cancel = driver.find_element(By.XPATH, Locator.overview_cancel_button)
        self.end_purchase = driver.find_element(By.XPATH, Locator.overview_finish_button)

    def locate_overview_title(self):
        """
        Method to get the Checkout: Overview title
        """
        return self.overview_title

    def locate_payment_info(self):
        """
        Method to locate the payment info
        """
        return self.payment_info

    def click_overview_cancel(self):
        """
        Method to locate and click overview cancel button
        """
        self.overview_cancel.click()
        sleep(TestData.DELAY)
        return self.overview_cancel

    def click_finish_button(self):
        """
        Method to locate and click the overview finish button
        """
        self.end_purchase.click()
        sleep(TestData.DELAY)
        return self.end_purchase
