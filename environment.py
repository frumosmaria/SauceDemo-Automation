from driver import Driver
from pages.login_page import LoginPage
from pages.sauce_home_page import SauceHomePage
from pages.sauce_login_page import SauceLoginPage
from pages.sauce_checkout_page import SauceCheckoutPage
from pages.sauce_cart_page import SauceCartPage


def before_all(context):
    print("I just started all the tests execution")
    context.browser = Driver()
    context.login_page = LoginPage()
    context.sauce_home_page = SauceHomePage()
    context.sauce_login_page = SauceLoginPage()
    context.sauce_checkout_page = SauceCheckoutPage()
    context.sauce_cart_page = SauceCartPage()

def after_all(context):
    print("I just finished all the tests execution")
    context.browser.close()