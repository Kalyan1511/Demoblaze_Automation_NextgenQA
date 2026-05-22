Feature: Cart Total Validation

  Scenario: Validate total amount in cart

    Given user has products inside cart
    Then total amount should be calculated correctly