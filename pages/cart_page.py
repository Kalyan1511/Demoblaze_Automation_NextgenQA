from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CartPage(BasePage):

    DELETE_BUTTON = (
        By.XPATH,
        "//a[text()='Delete']"
    )

    TOTAL_AMOUNT = (By.ID, "totalp")

    PLACE_ORDER = (
        By.XPATH,
        "//button[text()='Place Order']"
    )

    def __init__(self, driver):
        super().__init__(driver)
        self.wait.until(
            EC.presence_of_element_located(self.TOTAL_AMOUNT)
        )

    def delete_product(self):
        delete_element = self.wait.until(
            EC.element_to_be_clickable(self.DELETE_BUTTON)
        )
        delete_element.click()
        self.wait.until(EC.staleness_of(delete_element))

    def get_delete_button_count(self):
        return len(self.driver.find_elements(*self.DELETE_BUTTON))

    def wait_for_cart_items(self):
        self.wait.until(
            EC.visibility_of_element_located(self.DELETE_BUTTON)
        )

    def get_cart_total(self):
        return self.get_text(self.TOTAL_AMOUNT)

    def click_place_order(self):
        self.click_element(self.PLACE_ORDER)