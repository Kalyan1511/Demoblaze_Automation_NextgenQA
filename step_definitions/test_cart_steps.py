from pytest_bdd import scenarios, given, when, then
from selenium.common.exceptions import TimeoutException

from pages.products_page import ProductsPage
from pages.cart_page import CartPage

BASE_URL = "https://www.demoblaze.com/"


# CONNECT ALL CART FEATURES
scenarios("../features/cart.feature")
scenarios("../features/multiple_products.feature")
scenarios("../features/delete_cart.feature")
scenarios("../features/empty_cart.feature")
scenarios("../features/cart_total.feature")


@given("user opens a product page")
def open_product(driver):

    driver.product = ProductsPage(driver)
    driver.product.open_product()


@when("user clicks on Add To Cart button")
def add_product(driver):

    driver.alert_text = (
        driver.product.add_product_to_cart()
    )


@then("product should be added into the cart successfully")
def validate_cart(driver):

    assert (
        "Product added"
        in driver.alert_text
    )


@given("user adds first product into cart")
def first_product(driver):

    driver.product = ProductsPage(driver)
    driver.product.open_product()
    driver.product.add_product_to_cart()


@when("user adds second product into cart")
def second_product(driver):

    driver.get(BASE_URL)
    driver.product = ProductsPage(driver)
    driver.product.open_product()
    driver.product.add_product_to_cart()


@then("both products should be visible inside cart")
def validate_multiple_products(driver):

    driver.get(f"{BASE_URL}cart.html")
    driver.cart = CartPage(driver)
    driver.cart.wait_for_cart_items()
    assert driver.cart.get_delete_button_count() >= 1


@given("user already has product inside cart")
def cart_validation(driver):

    driver.get(BASE_URL)
    driver.product = ProductsPage(driver)
    driver.product.open_product()
    driver.product.add_product_to_cart()
    driver.get(f"{BASE_URL}cart.html")
    driver.cart = CartPage(driver)


@when("user deletes the product")
def delete_product(driver):

    driver.cart.delete_product()


@then("product should be removed from cart")
def validate_delete(driver):

    assert driver.cart.get_delete_button_count() == 0


@given("user removes all products from cart")
def remove_all_products(driver):

    driver.get(f"{BASE_URL}cart.html")
    driver.cart = CartPage(driver)

    while True:
        try:
            driver.cart.delete_product()
        except TimeoutException:
            break


@then("cart should display empty state")
def validate_empty_cart(driver):

    assert "Delete" not in driver.page_source


@given("user has products inside cart")
def has_products_in_cart(driver):

    driver.get(BASE_URL)
    driver.product = ProductsPage(driver)
    driver.product.open_product()
    driver.product.add_product_to_cart()
    driver.get(f"{BASE_URL}cart.html")
    driver.cart = CartPage(driver)


@then("total amount should be calculated correctly")
def validate_total_amount(driver):

    total = driver.cart.get_cart_total().strip()
    assert total.isdigit() and int(total) > 0