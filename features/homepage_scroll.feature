Feature: Homepage Scroll Validation

    Scenario: Validate homepage scrolling functionality

        Given user is on homepage
        When user scrolls down homepage
        Then homepage should scroll successfully