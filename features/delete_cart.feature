Feature: Delete Product From Cart

  Scenario: User removes product from cart

    Given user already has product inside cart
    When user deletes the product
    Then product should be removed from cart