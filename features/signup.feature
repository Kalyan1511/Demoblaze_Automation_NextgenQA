Feature: User Signup Functionality

  Scenario: Successful user signup with valid details

    Given user opens the signup modal
    When user enters valid signup credentials
    Then user account should be created successfully