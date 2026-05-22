from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, locator):
        retries = 3
        while retries:
            try:
                element = self.wait.until(
                    EC.element_to_be_clickable(locator)
                )
                try:
                    element.click()
                except ElementClickInterceptedException:
                    self.driver.execute_script("arguments[0].click();", element)
                return
            except (StaleElementReferenceException, ElementClickInterceptedException):
                retries -= 1
        raise

    def enter_text(self, locator, text):
        retries = 3
        while retries:
            try:
                element = self.wait.until(
                    EC.visibility_of_element_located(locator)
                )
                element.clear()
                element.send_keys(text)
                return
            except StaleElementReferenceException:
                retries -= 1
        raise

    def get_text(self, locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        return element.text

    def handle_alert(self):
        alert = self.wait.until(
            EC.alert_is_present()
        )

        alert_text = alert.text
        alert.accept()

        return alert_text

    def scroll_page(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

    def refresh_browser(self):
        self.driver.refresh()