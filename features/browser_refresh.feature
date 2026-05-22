Feature: Browser Refresh Session Validation

  Scenario: Validate user session after browser refresh

    Given user is logged into application
    When user refreshes the browser
    Then user session should remain active