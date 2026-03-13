from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class SauceCheckoutPage(BasePage):

    CHECKOUT_PAGE_URL = "https://www.saucedemo.com/checkout-step-one.html"
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    CHECKOUT_COMPLETE_CONTAINER = (By.ID, "checkout_complete_container")

    def is_url_correct(self) -> bool:
        return self.driver.current_url == self.CHECKOUT_PAGE_URL

    def fill_first_name(self, firstname):
        self.type(self.FIRST_NAME_INPUT, firstname)

    def fill_last_name(self, last_name):
        self.type(self.LAST_NAME_INPUT, last_name)

    def fill_zip_code(self, zip_code):
        self.type(self.ZIP_CODE_INPUT, zip_code)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def click_finish(self):
        self.click(self.FINISH_BUTTON)

    def get_complete_order_text(self):
        return self.get_element_text(self.CHECKOUT_COMPLETE_CONTAINER)