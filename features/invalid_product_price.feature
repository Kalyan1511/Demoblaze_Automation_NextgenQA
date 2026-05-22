Feature: Invalid Product Price Validation

  Scenario: Validate incorrect product price 

    Given user opens selected product
    Then product price should match incorrect expected value