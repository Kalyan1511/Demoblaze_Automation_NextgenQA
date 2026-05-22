Feature: Invalid Login Validation

  Scenario: Login should fail for invalid credentials

    Given user opens the login modal
    When user enters invalid login credentials
    Then invalid login alert should be displayed