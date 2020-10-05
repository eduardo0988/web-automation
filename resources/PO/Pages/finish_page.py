from selenium.webdriver.common.by import By

from resources.PO.Locators import Locator


class FinishPage():
    """
    Class wich contains the locators and methods for Checkout complete page
    """
    def __init__(self, driver):
        self.driver = driver
        # checkout complete page locators defining
        self.pony_express_image = driver.find_element(By.XPATH, Locator.pony_express_image)

    def locate_pony_image(self):
        """
        Method to locate the pony express image
        """
        return self.pony_express_image
