from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class SauceHomePage(BasePage):

    HOME_PAGE_URL = "https://www.saucedemo.com/inventory.html"
    UNIQUE_ELEMENT = (By.CSS_SELECTOR, "div.header_label > div.app-logo")
    PRODUCT_CONTAINER = (By.CSS_SELECTOR, "div.inventory_item")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn_primary")
    SHOPPING_CART_CONTAINER = (By.ID, "shopping_cart_container")


    def is_url_correct(self) -> bool:
        return self.driver.current_url == self.HOME_PAGE_URL

    def is_unique_element_visible(self) -> bool:
        return self.wait_for_element_visible(self.UNIQUE_ELEMENT, 30).is_displayed()

    def add_first_product_in_cart(self):
        list_of_products = self.driver.find_elements(*self.PRODUCT_CONTAINER)
        first_product = list_of_products[0]

        first_product_button = first_product.find_element(*self.ADD_TO_CART_BUTTON)
        first_product_button.click()

    def click_shopping_cart(self):
        self.click(self.SHOPPING_CART_CONTAINER)

