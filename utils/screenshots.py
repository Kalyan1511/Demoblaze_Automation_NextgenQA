import time


class ScreenshotUtils:

    @staticmethod
    def capture_screenshot(driver, name):

        screenshot_name = (
            f"screenshots/{name}_{int(time.time())}.png"
        )

        driver.save_screenshot(screenshot_name)