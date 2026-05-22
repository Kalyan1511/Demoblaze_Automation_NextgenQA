from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ProductsPage(BasePage):

    PHONES = (By.XPATH, "//a[text()='Phones']")
    LAPTOPS = (By.XPATH, "//a[text()='Laptops']")
    MONITORS = (By.XPATH, "//a[text()='Monitors']")

    PRODUCT = (
        By.XPATH,
        "//a[text()='Samsung galaxy s6']"
    )

    PRODUCT_DETAILS_HEADER = (
        By.XPATH,
        "//h2[text()='Samsung galaxy s6']"
    )

    ADD_TO_CART = (
        By.XPATH,
        "//a[text()='Add to cart']"
    )

    NEXT_BUTTON = (By.ID, "next2")

    PRODUCT_TITLE_CARDS = (By.CSS_SELECTOR, ".card-title")

    def click_phones_category(self):
        self.click_element(self.PHONES)

    def click_laptops_category(self):
        self.click_element(self.LAPTOPS)

    def click_monitors_category(self):
        self.click_element(self.MONITORS)

    def open_product(self):
        self.click_element(self.PRODUCT)
        self.wait.until(
            EC.visibility_of_element_located(self.PRODUCT_DETAILS_HEADER)
        )

    def add_product_to_cart(self):
        self.click_element(self.ADD_TO_CART)
        return self.handle_alert()

    def click_next_button(self):
        self.click_element(self.NEXT_BUTTON)
        self.wait.until(
            EC.visibility_of_all_elements_located(self.PRODUCT_TITLE_CARDS)
        )

    def get_product_titles(self):
        return [
            item.text
            for item in self.driver.find_elements(
                *self.PRODUCT_TITLE_CARDS
            )
        ]