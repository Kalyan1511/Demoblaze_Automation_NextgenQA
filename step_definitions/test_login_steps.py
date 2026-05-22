from pytest_bdd import scenarios, given, when, then

from pages.login_page import LoginPage


# CONNECT ALL LOGIN FEATURES
scenarios("../features/login.feature")
scenarios("../features/invalid_login.feature")
scenarios("../features/empty_login.feature")


@given("user opens the login modal")
def open_login(driver):

    driver.login = LoginPage(driver)
    driver.login.open_login_modal()


@when("user enters valid login credentials")
def login_user(driver):

    driver.login.login_valid_user()


@then("user should login successfully")
def validate_login(driver):

    assert "Welcome" in driver.page_source


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


@when("user keeps login fields empty")
def empty_login(driver):

    driver.login.click_element(
        driver.login.LOGIN_BUTTON
    )

    driver.alert_text = (
        driver.login.handle_alert()
    )


@then("empty login validation alert should be displayed")
def validate_empty_login(driver):

    assert (
        "Please fill out Username and Password"
        in driver.alert_text
    )