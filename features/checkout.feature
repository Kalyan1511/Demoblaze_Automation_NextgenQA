Feature: Checkout Functionality

  Scenario: User places order successfully

    Given user clicks on Place Order button
    When user enters valid purchase details
    Then order should be placed successfully