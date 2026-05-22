from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LogoutPage(BasePage):

    LOGOUT_BUTTON = (
        By.ID,
        "logout2"
    )

    def logout_application(self):
        self.click_element(self.LOGOUT_BUTTON)