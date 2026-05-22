from step_definitions.test_00_common_steps import ensure_logged_in

from pytest_bdd import scenarios, given, when, then

from pages.logout_page import LogoutPage


scenarios("../features/logout.feature")


@when("user clicks logout button")
def logout(driver):

    driver.logout = LogoutPage(driver)
    driver.logout.logout_application()


@then("user should logout successfully")
def validate_logout(driver):

    assert "Log in" in driver.page_source