from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):

    HOME_LINK = (By.XPATH, "//a[text()='Home ']")
    CONTACT_LINK = (By.XPATH, "//a[text()='Contact']")
    ABOUT_LINK = (By.XPATH, "//a[text()='About us']")
    CART_LINK = (By.ID, "cartur")

    def validate_homepage(self):
        return self.driver.title

    def click_cart(self):
        self.click_element(self.CART_LINK)