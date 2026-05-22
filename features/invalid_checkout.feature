Feature: Invalid Checkout Validation

  Scenario: User tries checkout with incomplete details

    Given user clicks on Place Order button
    When user submits incomplete purchase form
    Then validation message should be displayed