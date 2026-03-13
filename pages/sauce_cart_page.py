from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class SauceCartPage(BasePage):

    CART_PAGE_URL = "https://www.saucedemo.com/cart.html"
    CHECKOUT_BUTTON = (By.ID, "checkout")


    def is_url_correct(self) -> bool:
        return self.driver.current_url == self.CART_PAGE_URL

    def click_checkout_button(self):
        self.click(self.CHECKOUT_BUTTON)