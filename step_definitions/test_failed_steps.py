from pytest_bdd import scenarios, given, then

from pages.products_page import ProductsPage


scenarios("../features/invalid_product_price.feature")


@given("user opens selected product")
def open_product(driver):

    driver.product = ProductsPage(driver)
    driver.product.open_product()


@then("product price should match incorrect expected value")
def validate_wrong_price(driver):

    expected_price = "$99999"
    actual_price = "$360"

    if actual_price != expected_price:

        raise AssertionError(

            f"\n\n"
            f"PRODUCT PRICE VALIDATION FAILED\n"
            f"Expected Price : {expected_price}\n"
            f"Actual Price   : {actual_price}\n"
        )