from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from driver import Driver

class BasePage(Driver):

    DEFAULT_WAIT_TIMEOUT = 5

    def click(self, locator):
        self.wait_for_element(locator, self.DEFAULT_WAIT_TIMEOUT)
        self.driver.find_element(*locator).click()

    def type(self, locator, text):
        self.click(locator)
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)

    def get_element_text(self, locator):
        return self.wait_for_element(locator, self.DEFAULT_WAIT_TIMEOUT).text

    def wait_for_element(self, locator, wait_time) -> WebElement:
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_visible(self, locator, wait_time) -> WebElement:
        wait = WebDriverWait(self.driver, wait_time)
        return wait.until(EC.visibility_of_element_located(locator))

    # just for theoretically purpose
    def exit_from_driver(self):
        self.exit()