#This is the file that store all the login tests for the page: URL
Feature: tests for login functionality
  @login @positive @smoke
  Scenario: positive scenario
    Given I am on the login page
    When I insert an username "tomsmith"
    When I insert a password "SuperSecretPassword!"
    When I click on the login button
    Then The banner is displayed
    Then The message is "You logged into a secure area!"

  @smoke @skip @login @negative
  Scenario: negative scenario with incorrect username and password
    Given I am on the login page
    When I insert an username "bogdan12@gmail.com"
    When I insert a password "parolaITF"
    When I click on the login button
    Then The banner is displayed
    Then The message is "Your username is invalid!"

  @login @negative
  Scenario: negative scenario with correct username but wrong password
    Given I am on the login page
    When I insert an username "tomsmith"
    When I insert a password "parolaITF"
    When I click on the login button
    Then The banner is displayed
    Then The message is "Your password is invalid!"

  @login @positive @smoke @logout
  Scenario: positive scenario
    Given I am on the login page
    When I insert an username "tomsmith"
    When I insert a password "SuperSecretPassword!"
    When I click on the login button
    Then The banner is displayed
    Then The message is "You logged into a secure area!"
    When I click on logout button
    Then The banner is displayed
    Then The message is "You logged out of the secure area!"

