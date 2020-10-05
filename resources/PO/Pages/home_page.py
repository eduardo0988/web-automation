from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from resources.PO.Locators import Locator
from resources.PO.TestData import TestData

class HomePage():
    """
    Class wich contains the locators for Home Page objects
    """
    def __init__(self, driver):
        self.driver = driver
        # home page locators defining
        # self.menu_button = driver.find_element(By.ID, Locator.menu_button)
        """self.product_label = driver.find_element(By.ID, Locator.product_label)
        self.burger_button = driver.find_element(By.CLASS_NAME, Locator.burger_button)
        self.logout_button = driver.find_element(By.ID, Locator.logout_button)"""

        """back_pack = "/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/button"
        back_pack_id = "item_4_title_link"
        bike_light = "/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/button"
        bike_light_id = "item_0_title_link"
        red_tshirt = "/html/body/div/div[2]/div[2]/div/div[2]/div/div[6]/div[3]/button"
        red_tshirt_id = "item_3_title_link"
        remove_backpack = "/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/button"""


    """def menu(self):
        """
        Method to locate the menu button in home page.
        """
        return self.menu_button"""
