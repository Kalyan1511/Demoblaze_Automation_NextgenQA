Feature: Contact Form Validation

  Scenario: User sends contact message successfully

    Given user opens contact modal
    When user enters contact form details
    Then contact success alert should be displayed