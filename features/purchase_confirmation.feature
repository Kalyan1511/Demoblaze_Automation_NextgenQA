Feature: Purchase Confirmation Validation

  Scenario: Validate successful purchase confirmation

    Given user completes purchase successfully
    Then confirmation message should be displayed