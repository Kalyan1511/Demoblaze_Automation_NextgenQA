from step_definitions.test_00_common_steps import homepage

from pytest_bdd import scenarios, given, then

from pages.home_page import HomePage


scenarios("../features/navigation_links.feature")


@then("all navigation links should work properly")
def validate_links(driver):

    assert "Home" in driver.page_source
    assert "Contact" in driver.page_source
    assert "Cart" in driver.page_source