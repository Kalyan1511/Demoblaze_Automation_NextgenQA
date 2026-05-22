import json
import os
import pytest
import step_definitions.test_00_common_steps
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

pytest_plugins = ["step_definitions.test_00_common_steps"]

BASE_URL = "https://www.demoblaze.com/"

@pytest.fixture(scope="session")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    driver.get(BASE_URL)

    yield driver

    driver.quit()


def pytest_sessionstart(session):
    os.makedirs("reports", exist_ok=True)
    os.makedirs("screenshots", exist_ok=True)
    os.makedirs("allure-results", exist_ok=True)


@pytest.fixture(autouse=True)
def session_user(driver):
    with open("data/user_data.json") as file:
        user_data = json.load(file)
    driver.user_name = user_data.get("username", "Sandeep")
    driver.user_email = user_data.get("email", "test@gmail.com")
    yield


@pytest.fixture(autouse=True)
def reset_application(driver):
    driver.get(BASE_URL)
    yield