Feature: Product Category Validation

  Scenario: Validate phone category products

    Given user is on homepage
    When user clicks Phones category
    Then phone products should be displayed