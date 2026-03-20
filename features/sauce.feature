Feature: all scenarios related to saucedemo.com
  @sauce
  Scenario: Positive order
    Given I am on saucedemo login page
    When I insert a sauce username "standard_user"
    When I insert a sauce password "secret_sauce"
    When I click on sauce login button
    Then I landed on sauce home page
    When I add first product to the cart
    When I click on shopping cart
    Then The cart page is loaded
    When I click on checkout button
    Then The checkout page is loaded
    When I fill my first name "daniel"
    When I fill my last name "ionas"
    When I fill my zipcode "770077"
    When I click on continue button
    When I click on finish button
    Then The order message is "Thank you for your order!"
