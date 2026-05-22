from step_definitions.test_00_common_steps import ensure_logged_in
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pytest_bdd import scenarios, given, when, then


scenarios("../features/browser_refresh.feature")


@when("user refreshes the browser")
def refresh_browser(driver):

    driver.refresh()
    WebDriverWait(driver, 10).until(
        lambda d: "Welcome" in d.page_source
    )


@then("user session should remain active")
def validate_session(driver):

    assert "Welcome" in driver.page_source