from pytest_bdd import scenarios, given, when, then

from pages.contact_page import ContactPage


scenarios("../features/contact.feature")


@given("user opens contact modal")
def open_contact(driver):

    driver.contact = ContactPage(driver)
    driver.contact.open_contact_modal()


@when("user enters contact form details")
def send_message(driver):

    driver.alert_text = (
        driver.contact.send_contact_message(
            getattr(driver, "user_name", "Sandeep")
        )
    )


@then("contact success alert should be displayed")
def validate_contact(driver):

    assert (
        "Thanks"
        in driver.alert_text
    )