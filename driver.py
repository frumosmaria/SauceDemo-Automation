from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Driver:

    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    #this option was added to keep alive Chrome process to avoid closing Google Meets share screen
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--guest")
    driver = webdriver.Chrome(options=chrome_options)

    #driverFox = webdriver.Firefox()
    #driverEdge = webdriver.Edge()

    def close(self):
        print("Closing driver")
        #self.driver.quit()

    # def exit(self):
    #     self.driver.close()