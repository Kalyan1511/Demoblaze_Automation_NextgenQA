from pytest_bdd import scenarios, given, when, then

from pages.signup_page import SignupPage


# CONNECT BOTH FEATURES
scenarios("../features/signup.feature")
scenarios("../features/existing_signup.feature")


@given("user opens the signup modal")
def open_signup(driver):

    driver.signup = SignupPage(driver)
    driver.signup.open_signup_modal()


@when("user enters valid signup credentials")
def signup_user(driver):

    driver.alert_text = (
        driver.signup.signup_new_user()
    )


@then("user account should be created successfully")
def validate_signup(driver):

    assert (
        "Sign up successful"
        in driver.alert_text
    )


@when("user enters already registered credentials")
def duplicate_signup(driver):

    driver.alert_text = (
        driver.signup.signup_existing_user()
    )


@then("duplicate signup alert should be displayed")
def validate_duplicate_signup(driver):

    assert (
        "already exist"
        in driver.alert_text
    )