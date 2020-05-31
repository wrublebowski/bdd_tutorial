Feature: Test navigation through pages

  Scenario: Go from homepage to pricing
    Given I start on the homepage
    When I click on link with text: "PRICING"
    Then Im in pricing page
    And Scroll page by "300"

  Scenario: Go from pricing to login page
    Given I start on pricing page
    When I click on link with text: "SIGN IN"
    Then Im on login page