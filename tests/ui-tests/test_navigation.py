import pytest
from selenium import webdriver

from models.main_page import MainPage


class TestNavigation:

    @pytest.fixture
    def driver(self):
        mobile_emulation = {"deviceName": "Nexus 5"}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        driver = webdriver.Chrome(chrome_options)
        driver.implicitly_wait(10)
        yield driver
        driver.quit()


    def test_search_and_select_streamer(self, driver):
        twitch_page = MainPage(driver)
        twitch_page.open_main_page()
        twitch_page.search_for("StarCraft II")
        twitch_page.scroll()
        twitch_page.select_first_streamer()
        twitch_page.take_a_screenshot()

