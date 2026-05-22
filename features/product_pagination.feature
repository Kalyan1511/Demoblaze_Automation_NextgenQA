Feature: Product Pagination Validation

  Scenario: Validate next product page navigation

    Given user is on homepage
    When user clicks next pagination button
    Then next set of products should be displayed