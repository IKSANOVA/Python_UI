from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from selenium.common.exceptions import NoSuchElementException
import allure


class MainPage(BasePage):
    SEARCH = (By.NAME, "search")
    H3 = (By.TAG_NAME, "h3")
    BUTTON = (By.CSS_SELECTOR, "#search > span > button")
    TITLE = "Your Store"

    @allure.step("Проверка элемента поиск")
    def check_search(self):
        self._element(self.SEARCH)

    @allure.step("Проверка элемента заголовок")
    def check_h3(self):
        self._element(self.H3)

    @allure.step("Проверка элемента кнопка")
    def check_button(self):
        self._element(self.BUTTON)

    @allure.step("Проверка клика на кнопку")
    def check_click_button(self):
        self._click(self.BUTTON)

    @allure.step("Проверка элемента заголовок")
    def check_title(self):
        self._check_title(self.TITLE)
