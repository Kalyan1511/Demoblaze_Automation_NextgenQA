Feature: Empty Login Validation

  Scenario: User tries login without credentials

    Given user opens the login modal
    When user keeps login fields empty
    Then empty login validation alert should be displayed