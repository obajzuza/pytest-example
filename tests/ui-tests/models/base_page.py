import datetime

from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    screenshots_destination_path = ""

    def scroll(self):
        ActionChains(self.driver).scroll_by_amount(0, 100).perform()

    def take_a_screenshot(self):
        self.driver.save_screenshot(f"{self.screenshots_destination_path}/{datetime.datetime.now()}.png")