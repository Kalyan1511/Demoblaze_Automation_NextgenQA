from pytest_bdd import scenarios, given, when, then

from pages.login_page import LoginPage


scenarios("../features/invalid_login.feature")


@given("user opens the login modal")
def open_login(driver):

    driver.login = LoginPage(driver)
    driver.login.open_login_modal()


@when("user enters invalid login credentials")
def invalid_login(driver):

    driver.alert_text = (
        driver.login.login_invalid_user()
    )


@then("invalid login alert should be displayed")
def validate_invalid_login(driver):

    assert (
        "Wrong password"
        in driver.alert_text
    )