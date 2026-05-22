from step_definitions.test_00_common_steps import homepage

from pytest_bdd import scenarios, given, when, then

from pages.products_page import ProductsPage


scenarios("../features/product_category.feature")
scenarios("../features/product_details.feature")
scenarios("../features/product_pagination.feature")


@given("user opens selected product")
def selected_product(driver):

    driver.product = ProductsPage(driver)
    driver.product.open_product()


@then("product details should be displayed properly")
def validate_product(driver):

    assert (
        "Samsung galaxy s6"
        in driver.page_source
    )


@when("user clicks Phones category")
def phone_category(driver):

    driver.product = ProductsPage(driver)
    driver.product.click_phones_category()


@then("phone products should be displayed")
def validate_phone_products(driver):

    assert "Samsung" in driver.page_source


@when("user clicks next pagination button")
def pagination(driver):

    driver.product.click_next_button()


@then("next set of products should be displayed")
def validate_pagination(driver):

    assert len(driver.product.get_product_titles()) > 0