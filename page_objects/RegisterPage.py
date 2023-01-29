from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from selenium.common.exceptions import NoSuchElementException
import allure

class RegisterPage(BasePage):
    FIRSTNAME = (By.NAME, "firstname")
    LASTNAME = (By.NAME, "lastname")
    EMAIL = (By.NAME, "email")
    TELEPHONE = (By.NAME, "telephone")
    PASS = (By.NAME, "password")
    CONFPASS = (By.NAME, "confirm")


    @allure.step("Проверка элемента Имя")
    def check_firstname(self):
        self._element(self.FIRSTNAME)


    @allure.step("Проверка элемента Фамилия")
    def check_lastname(self):
        self._element(self.LASTNAME)


    @allure.step("Проверка элемента e-mail")
    def check_email(self):
        self._element(self.EMAIL)
        

    @allure.step("Проверка элемента телефон")
    def check_telephon(self):
        self._element(self.TELEPHONE)
