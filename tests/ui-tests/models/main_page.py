from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from models.base_page import BasePage


class MainPage(BasePage):
    url = "https://m.twitch.tv/"

    # elements
    def bottom_bar_buttons(self):
        return self.driver.find_elements(By.CLASS_NAME, "ScInteractableBase-sc-ofisyf-0 ScInteractableDefault-sc-ofisyf-1 iCUBCA jSoDPq InjectLayout-sc-1i43xsx-0 juMFQg")

    def close_login_banner(self):
        return WebDriverWait(self.driver, timeout=2).until(EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Aktywuj, aby zamknąć okno']")))

    def cookies_consent_button(self, option):
        return self.driver.find_element(By.XPATH, f"//button[.='{option}']")

    def search_button(self):
        return self.driver.find_element(By.CLASS_NAME, "tw-input--large")

    def search_input(self):
        return self.driver.find_element(By.TAG_NAME, "input")

    def streamers(self):
        return self.driver.find_elements(By.XPATH, "//button[@class='ScCoreLink-sc-16kq0mq-0 eMycWd InjectLayout-sc-1i43xsx-0 ggvZjN tw-link']")

    def browse_button(self):
        return self.driver.find_element(By.XPATH, "//a[@href='/directory']")

    def wait_for_chat_options_button(self):
        return WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Ustawienia czatu']")))

    # methods
    def open_main_page(self):
        self.driver.get(self.url)
        self.close_login_banner().click()
        self.cookies_consent_button("Odrzuć").click()

    def search_for(self, search_text: str):
        self.browse_button().click()
        self.search_button().click()
        self.search_input().send_keys(search_text)
        self.search_input().send_keys(Keys.RETURN)

    def select_first_streamer(self):
        self.streamers()[0].click()


