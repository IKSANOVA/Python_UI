from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from selenium.common.exceptions import NoSuchElementException


class AdminPage(BasePage):
    LOGO = (By.CSS_SELECTOR, "#header-logo>a>img")
    HELP_TEXT = (By.CSS_SELECTOR, "h1.panel-title")
    FORGOT_PASSWORD = (By.CSS_SELECTOR, "span.help-block")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "span.help-block")
    INPUT_LOGIN = (By.CSS_SELECTOR, "#input-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type=submit]")


    def check_logo(self):
        self._element(self.LOGO)


    def check_help_text(self):
        self._element(self.HELP_TEXT)


    def check_forgot_password(self):
        self._element(self.FORGOT_PASSWORD)


    def check_login_button(self):
        self._element(self.LOGIN_BUTTON)


    def login(self, username, password):
        self._element(self.INPUT_LOGIN).clear()
        self._element(self.INPUT_LOGIN).send_keys(username)
        self._element(self.INPUT_PASSWORD).clear()
        self._element(self.INPUT_PASSWORD).send_keys(password)
        self._element(self.LOGIN_BUTTON).click()
