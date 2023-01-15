from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from selenium.common.exceptions import NoSuchElementException


class RegisterPage(BasePage):
    FIRSTNAME = (By.NAME, "firstname")
    LASTNAME = (By.NAME, "lastname")
    EMAIL = (By.NAME, "email")
    TELEPHONE = (By.NAME, "telephone")
    PASS = (By.NAME, "password")
    CONFPASS = (By.NAME, "confirm")

    def check_firstname(self):
        self._element(self.FIRSTNAME)

    def check_lastname(self):
        self._element(self.LASTNAME)

    def check_email(self):
        self._element(self.EMAIL)

    def check_telephon(self):
        self._element(self.TELEPHONE)
