Feature: User Login Functionality

  Scenario: Successful login with valid credentials

    Given user opens the login modal
    When user enters valid login credentials
    Then user should login successfully