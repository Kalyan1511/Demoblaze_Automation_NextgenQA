from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ContactPage(BasePage):

    CONTACT_LINK = (
        By.XPATH,
        "//a[text()='Contact']"
    )

    EMAIL = (By.ID, "recipient-email")
    NAME = (By.ID, "recipient-name")
    MESSAGE = (By.ID, "message-text")

    SEND_MESSAGE = (
        By.XPATH,
        "//button[text()='Send message']"
    )

    def open_contact_modal(self):
        self.click_element(self.CONTACT_LINK)

    def send_contact_message(self, name):

        self.enter_text(
            self.EMAIL,
            "test@gmail.com"
        )

        self.enter_text(
            self.NAME,
            name
        )

        self.enter_text(
            self.MESSAGE,
            "Testing ecommerce contact form"
        )

        self.click_element(self.SEND_MESSAGE)

        return self.handle_alert()