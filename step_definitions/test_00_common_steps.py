from pytest_bdd import given

from pages.home_page import HomePage
from pages.login_page import LoginPage

BASE_URL = "https://www.demoblaze.com/"


@given("user is on homepage")
def homepage(driver):
    driver.get(BASE_URL)
    driver.home = HomePage(driver)


@given("user is logged into application")
def ensure_logged_in(driver):
    driver.login = LoginPage(driver)

    if "Welcome" not in driver.page_source:
        driver.login.open_login_modal()
        driver.login.login_valid_user()

    assert "Welcome" in driver.page_source 