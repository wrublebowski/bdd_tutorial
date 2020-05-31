Feature: Test navigation through pages

  Scenario: Go from homepage to pricing
    Given I start on the homepage
    When I click on navigation link with text: "Pricing"
    Then Im in pricing page
    And Scroll page by "300"
    And Wait for choose_btn to load
    Then I click on button with text: "Choose"

  Scenario: Go from pricing to login page
    Given I start on pricing page
    When I click on navigation link with text: "Sign in"
    Then Im on login page

  Scenario: Send some text to login
    Given I start on the homepage
    When I click on navigation link with text: "Sign in"
    And Im on login page
    Then I enter email "mietek@nagietek.pl" and password "hujemuje"
    And I click on login to submit