Feature: Multiple Product Cart Validation

  Scenario: User adds multiple products into cart

    Given user adds first product into cart
    When user adds second product into cart
    Then both products should be visible inside cart