Feature: Shopping Cart Functionality

  Scenario: User adds product into cart successfully

    Given user opens a product page
    When user clicks on Add To Cart button
    Then product should be added into the cart successfully