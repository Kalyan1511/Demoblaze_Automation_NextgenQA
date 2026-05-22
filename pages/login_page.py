import json

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_LINK = (By.ID, "login2")
    USERNAME = (By.ID, "loginusername")
    PASSWORD = (By.ID, "loginpassword")

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[text()='Log in']"
    )

    def open_login_modal(self):
        self.click_element(self.LOGIN_LINK)

    def login_valid_user(self):

        with open("data/user_data.json") as file:
            user_data = json.load(file)

        self.enter_text(
            self.USERNAME,
            user_data["username"]
        )

        self.enter_text(
            self.PASSWORD,
            user_data["password"]
        )

        self.click_element(self.LOGIN_BUTTON)
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.ID, "nameofuser"),
                user_data["username"]
            )
        )

    def login_invalid_user(self):

        self.enter_text(
            self.USERNAME,
            "wrong_user"
        )

        self.enter_text(
            self.PASSWORD,
            "wrong_password"
        )

        self.click_element(self.LOGIN_BUTTON)

        return self.handle_alert()