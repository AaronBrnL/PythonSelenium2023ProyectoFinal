import logging
import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from src.page_objects.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(ProductPage, self).__init__(driver, wait_driver)

    def iphone_search(self, input_search: str):
        logging.info(f"Wait text be present, locator  {input_search} and click in btn")
        self.element("input_search").wait_clickable().clear()
        self.element("input_search").wait_clickable().send_keys(input_search)
        self.element("btn_search").wait_clickable().click()
        self.element("iphone_product").wait_clickable().click()
        self.element("btn_add_Cart").wait_clickable().click()
        self.element("cart").wait_clickable().click()

        time.sleep(5)
