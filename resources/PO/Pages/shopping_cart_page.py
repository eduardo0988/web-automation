from selenium.webdriver.common.by import By
from time import sleep

from resources.PO.Locators import Locator
from resources.PO.TestData import TestData


class ShoppingCartPage():
    """
    Class wich contains the locators and methods for Shopping Cart objects
    """
    def __init__(self, driver):
        self.driver = driver
        # shopping cart page locators defining
        self.cart_title = driver.find_element(By.XPATH, Locator.cart_title)
        self.checkout_button = driver.find_element(By.XPATH, Locator.checkout_button)
        self.remove_first_item = driver.find_element(By.XPATH, Locator.remove_first_element)
        self.items_in_cart = driver.find_element(By.XPATH, Locator.mini_cart_qty)
        self.items_in_cart_list = driver.find_element(By.XPATH, Locator.cart_qty)

    def find_cart_title(self):
        """
        Method to locate the cart title ("Your Cart")
        """
        return self.cart_title

    def click_checkout_button(self):
        """
        Method to locate and click the checkout button
        """
        self.checkout_button.click()
        return self.checkout_button

    def remove_item_one(self):
        """
        Method to remove the first item on shopping list
        """
        self.remove_first_item.click()
        sleep(TestData.DELAY)
        return self.remove_first_item

    def get_items_cart_qty(self):
        """
        Method to locate the cart icon with the quantity of items in cart
        """
        return self.items_in_cart

    def get_items_cart_list(self):
        """
        Method to locate the cart list and get the quantity of items
        """
        return self.items_in_cart_list
