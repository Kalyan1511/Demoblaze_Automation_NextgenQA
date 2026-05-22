from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):

    NAME = (By.ID, "name")
    COUNTRY = (By.ID, "country")
    CITY = (By.ID, "city")
    CARD = (By.ID, "card")
    MONTH = (By.ID, "month")
    YEAR = (By.ID, "year")

    PURCHASE_BUTTON = (
        By.XPATH,
        "//button[text()='Purchase']"
    )

    SUCCESS_MESSAGE = (
        By.XPATH,
        "//h2[text()='Thank you for your purchase!']"
    )

    def fill_checkout_form(self, name):

        self.enter_text(self.NAME, name)
        self.enter_text(self.COUNTRY, "India")
        self.enter_text(self.CITY, "Chennai")
        self.enter_text(self.CARD, "123456789")
        self.enter_text(self.MONTH, "May")
        self.enter_text(self.YEAR, "2026")

    def click_purchase(self):
        self.click_element(self.PURCHASE_BUTTON)