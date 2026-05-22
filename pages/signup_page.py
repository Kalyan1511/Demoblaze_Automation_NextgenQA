import json
import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SignupPage(BasePage):

    SIGNUP_LINK = (By.ID, "signin2")
    USERNAME = (By.ID, "sign-username")
    PASSWORD = (By.ID, "sign-password")

    SIGNUP_BUTTON = (
        By.XPATH,
        "//button[text()='Sign up']"
    )

    def open_signup_modal(self):
        self.click_element(self.SIGNUP_LINK)

    def signup_new_user(self):

        username = f"user_{int(time.time())}"
        password = "Test@123"

        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)

        with open("data/user_data.json", "w") as file:
            json.dump(
                {
                    "username": username,
                    "password": password
                },
                file,
                indent=4
            )

        self.click_element(self.SIGNUP_BUTTON)

        return self.handle_alert()

    def signup_existing_user(self):

        with open("data/user_data.json") as file:
            user_data = json.load(file)

        self.enter_text(self.USERNAME, user_data["username"])
        self.enter_text(self.PASSWORD, user_data["password"])

        self.click_element(self.SIGNUP_BUTTON)

        return self.handle_alert()