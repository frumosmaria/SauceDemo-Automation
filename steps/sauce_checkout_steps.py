from behave import *

@then('The cart page is loaded')
def step_impl(context):
    assert context.sauce_cart_page.is_url_correct(), "Cart URL is not the same"


@when('I click on checkout button')
def step_impl(context):
    context.sauce_cart_page.click_checkout_button()

@then('The checkout page is loaded')
def step_impl(context):
    assert context.sauce_checkout_page.is_url_correct(), "Checkout URL is not the same"

@when('I fill my first name "{first_name}"')
def step_impl(context, first_name):
    context.sauce_checkout_page.fill_first_name(first_name)

@when('I fill my last name "{last_name}"')
def step_impl(context, last_name):
    context.sauce_checkout_page.fill_last_name(last_name)

@when('I fill my zipcode "{zip_code}"')
def step_impl(context, zip_code):
    context.sauce_checkout_page.fill_zip_code(zip_code)

@when('I click on continue button')
def step_impl(context):
    context.sauce_checkout_page.click_continue()

@when('I click on finish button')
def step_impl(context):
    context.sauce_checkout_page.click_finish()

@then('The order message is "{message}"')
def step_impl(context, message):
    assert message in context.sauce_checkout_page.get_complete_order_text(), "Message is not the same"