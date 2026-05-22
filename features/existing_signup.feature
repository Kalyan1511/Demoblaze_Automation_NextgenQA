Feature: Existing User Signup Validation

  Scenario: User tries signup using existing credentials

    Given user opens the signup modal
    When user enters already registered credentials
    Then duplicate signup alert should be displayed