from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SauceLoginPage(BasePage):

    LOGIN_PAGE_URL = "https://www.saucedemo.com/"

    EMAIL_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def navigate_to_page(self):
        self.driver.get(self.LOGIN_PAGE_URL)

    def set_email(self, email):
        #self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.type(self.EMAIL_INPUT, email)

    def set_password(self, password):
        #self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.type(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)