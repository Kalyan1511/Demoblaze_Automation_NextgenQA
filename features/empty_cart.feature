Feature: Empty Cart Validation

  Scenario: Validate cart becomes empty after deletion

    Given user removes all products from cart
    Then cart should display empty state