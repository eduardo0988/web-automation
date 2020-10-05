import os
import datetime
import slash

from selenium import webdriver
from time import sleep

from resources.PO.Locators import Locator
from resources.PO.TestData import TestData


class BaseTest(slash.Test):
    """
    Class to contain all logic common to all tests scripts
    """
    def before(self):
        """
        Setup the browser and validate that we are in the login page
        """
        self.driver = webdriver.Firefox(TestData.GECKO_PATH, service_log_path=TestData.GECKO_LOG_PATH)
        slash.logger.info("Run Started at:{}".format(datetime.datetime.now()))
        slash.logger.info("Chrome Environment Set Up")
        slash.logger.info("-"*80)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get(TestData.BASE_URL)
        self.driver.set_page_load_timeout(30)

        try:
            # Validating page title with the expected.
            assert self.driver.title == TestData.EXPECTED_TITLE
            slash.logger.info("Login page loaded successfully")
        except Exception as exc:
            slash.add_failure("{}".format(exc))

    def after(self):
        """
        Tear Down method. Logout from saucedemo page, closes all the browser instances and then quit
        """
        if self.driver is not None:
            slash.logger.info("-"*80)
            slash.logger.info("Test Environment Destroyed")
            slash.logger.info("Run Completed at:{}".format(datetime.datetime.now()))
            self.driver.close()
            self.driver.quit()
