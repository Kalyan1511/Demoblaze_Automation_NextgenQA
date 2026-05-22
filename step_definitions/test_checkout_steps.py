from pytest_bdd import scenarios, given, when, then

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


# CONNECT ALL CHECKOUT FEATURES
scenarios("../features/checkout.feature")
scenarios("../features/invalid_checkout.feature")
scenarios("../features/purchase_confirmation.feature")


@given("user clicks on Place Order button")
def place_order(driver):

    driver.get("https://www.demoblaze.com/cart.html")
    driver.cart = CartPage(driver)
    driver.cart.click_place_order()


@when("user enters valid purchase details")
def valid_checkout(driver):

    driver.checkout = CheckoutPage(driver)
    driver.checkout.fill_checkout_form(getattr(driver, "user_name", "Sandeep"))
    driver.checkout.click_purchase()


@then("order should be placed successfully")
def validate_checkout(driver):

    assert (
        "Thank you for your purchase!"
        in driver.page_source
    )


@when("user submits incomplete purchase form")
def invalid_checkout(driver):

    driver.checkout = CheckoutPage(driver)
    driver.checkout.click_purchase()
    driver.alert_text = driver.checkout.handle_alert()


@then("validation message should be displayed")
def validate_invalid_checkout(driver):

    assert "Please fill out Name and Creditcard" in driver.alert_text


@given("user completes purchase successfully")
def purchase_complete(driver):

    driver.get("https://www.demoblaze.com/cart.html")
    driver.cart = CartPage(driver)
    driver.cart.click_place_order()

    driver.checkout = CheckoutPage(driver)
    driver.checkout.fill_checkout_form(getattr(driver, "user_name", "Sandeep"))
    driver.checkout.click_purchase()


@then("confirmation message should be displayed")
def validate_confirmation(driver):

    assert (
        "Thank you for your purchase!"
        in driver.page_source
    )