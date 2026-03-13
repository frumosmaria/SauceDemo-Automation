from behave import *

@given('I am on saucedemo login page')
def step_impl(context):
    context.sauce_login_page.navigate_to_page()

@when('I insert a sauce username "{username}"')
def step_impl(context, username):
    context.sauce_login_page.set_email(username)

@when('I insert a sauce password "{password}"')
def step_impl(context, password):
    context.sauce_login_page.set_password(password)

@when('I click on sauce login button')
def step_impl(context):
    context.sauce_login_page.click_login()

@then('I landed on sauce home page')
def step_impl(context):
    assert context.sauce_home_page.is_url_correct(), "URL is not the same"

@then('The unique element is displayed')
def step_impl(context):
    assert context.sauce_home_page.is_unique_element_visible(), "Element is not visible on homepage"

@when('I add first product to the cart')
def step_impl(context):
    context.sauce_home_page.add_first_product_in_cart()

@when('I click on shopping cart')
def step_impl(context):
    context.sauce_home_page.click_shopping_cart()