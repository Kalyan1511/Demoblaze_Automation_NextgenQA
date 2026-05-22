Feature: Logout Validation

  Scenario: User logs out successfully

    Given user is logged into application
    When user clicks logout button
    Then user should logout successfully