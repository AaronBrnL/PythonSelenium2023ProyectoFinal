import logging
import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from src.page_objects.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(SearchPage, self).__init__(driver, wait_driver)

    def search(self, input_search: str):
        logging.info(f"Wait text be present, locator  {input_search} and click in btn")
        self.element("input_search").wait_clickable().send_keys(input_search)
        self.element("btn_search").wait_clickable().click()
        time.sleep(2)

    def get_message(self):
        return self.element("message").wait_visible().text
