from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

from resources.PO.Locators import Locator
from resources.PO.TestData import TestData


class LoginPage():
    """
    Class wich contains the locators for Login Page objects
    """
    def __init__(self, driver):
        self.driver = driver
        # login locators defining
        self.username = driver.find_element(By.ID, Locator.user_name)
        self.password = driver.find_element(By.ID, Locator.password)
        self.login = driver.find_element(By.ID, Locator.login_button)
        self.log_bot = driver.find_element(By.XPATH, Locator.bot_image)

    def enter_username(self, user=TestData.USERS[0]):
        """
        Method to locate and send the user_name to login page.

        :param user: string, user name (Default value is standard_user)
        """
        self.username.clear()
        self.username.click()
        self.username.send_keys(user)
        return self.username

    def enter_password(self):
        """
        Method to locate and send the password to login page.
        """
        self.password.clear()
        self.password.click()
        self.password.send_keys(TestData.PASSWORD)
        sleep(TestData.DELAY)
        return self.password

    def click_login(self):
        """
        Method to locate and click login button
        """
        self.login.click()
        return self.login

    def scroll_page(self):
        """
        Method to scroll down and up the page
        """
        scroll_down = self.driver.find_element_by_tag_name("html")
        scroll_down.send_keys(Keys.END)
        sleep(TestData.DELAY)
        scroll_down.send_keys(Keys.CONTROL + Keys.HOME)
        sleep(TestData.DELAY)
        return True

    def bot_image(self):
        """
        Method to locate the bot image in the login page
        """
        return self.bot_image
