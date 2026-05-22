from step_definitions.test_00_common_steps import homepage

from pytest_bdd import scenarios, given, when, then

from pages.home_page import HomePage


scenarios("../features/home_navigation.feature")
scenarios("../features/homepage_scroll.feature")


@when("user scrolls down homepage")
def scroll_homepage(driver):

    driver.home.scroll_page()


@then("homepage should scroll successfully")
def validate_scroll(driver):

    assert driver.execute_script(
        "return window.pageYOffset;"
    ) > 0


@then("homepage navigation should work properly")
def validate_navigation(driver):

    assert "STORE" in driver.title