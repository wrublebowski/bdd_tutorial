Feature: Tests that pages have correct content

  Scenario: We check if Pricing page has a correct header and title
    Given I start on pricing page
    Then The header is present on page
    And The pricing header has content: "Pricing"
    And The page title has content: "Pricing"

  Scenario: We check if Home page has a correct title
    Given I start on the homepage
    Then The page title has content: "Push"