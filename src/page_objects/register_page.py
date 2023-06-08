import logging
import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from src.page_objects.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(RegisterPage, self).__init__(driver, wait_driver)

    def register(self, firstName: str, lastName: str, email: str, telephone: str, password: str, password_confirm: str):
        logging.info(f"Wait text be present, locator  {firstName} and lastName *****")
        self.element("first_name").wait_clickable().send_keys(firstName)
        self.element("last_name").wait_clickable().send_keys(lastName)
        self.element("email").wait_clickable().clear()
        self.element("email").wait_clickable().send_keys(email)
        self.element("telephone").wait_clickable().send_keys(telephone)
        self.element("password").wait_clickable().clear()
        self.element("password").wait_clickable().send_keys(password)
        self.element("password_confirm").wait_clickable().send_keys(password_confirm)
        self.element("suscribe_yes").wait_clickable().click()
        self.element("privacy_policy").wait_clickable().click()
        self.element("btn_continue").wait_clickable().click()
        self.element("account_created_btn_continue").wait_clickable().click()
        time.sleep(2)



