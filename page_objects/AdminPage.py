from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from selenium.common.exceptions import NoSuchElementException
import allure


class AdminPage(BasePage):
    LOGO = (By.CSS_SELECTOR, "#header-logo>a>img")
    HELP_TEXT = (By.CSS_SELECTOR, "h1.panel-title")
    FORGOT_PASSWORD = (By.CSS_SELECTOR, "span.help-block")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "span.help-block")
    INPUT_LOGIN = (By.CSS_SELECTOR, "#input-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type=submit]")
    CATALOG_BUTTON = (By.CSS_SELECTOR, "#menu-catalog>a")
    CATALOG_PRODUCTS_BUTTON = (By.CSS_SELECTOR, "#menu-catalog>ul>:nth-child(2)")
    ADD_NEW_BUTTON = (By.CSS_SELECTOR, "div.pull-right>:nth-child(2)")
    CATEGORY_NAME = (By.CSS_SELECTOR, "#input-name1")
    DEVICE_DESCRIPTION = (By.CSS_SELECTOR, ".note-editable")
    META_TAG = (By.CSS_SELECTOR, "#input-meta-title1")
    SAVE_DEVICE = (By.CSS_SELECTOR, "button[data-original-title=Save]")
    DATA_TAB = (By.XPATH, "//*[text()='Data']")
    MODEL_NAME = (By.CSS_SELECTOR, "#input-model")
    LAST_PAGE = (By.XPATH, "//*[text()='>|']")
    DEVICE_FOR_DELETE = (By.CSS_SELECTOR, "tbody>tr:nth-child(1)>td>input")
    DEVICE_NAME = (By.CSS_SELECTOR, "tbody>tr>td:nth-child(3)")
    LAST_DEVICE = (By.CSS_SELECTOR, "tbody>tr:last-child>td:nth-child(3)")
    DELETE_BUTTON = (By.CSS_SELECTOR, "div.pull-right>:nth-child(4)")

    @allure.step("Проверка отображения логотипа")
    def check_logo(self):
        self._element(self.LOGO)


    @allure.step("Проверка текста помощи")
    def check_help_text(self):
        self._element(self.HELP_TEXT)

    @allure.step("Проверка ссылки забыл пароль")
    def check_forgot_password(self):
        self._element(self.FORGOT_PASSWORD)


    @allure.step("Проверка кнопки Входа")
    def check_login_button(self):
        self._element(self.LOGIN_BUTTON)


    @allure.step("Проверка ввода логина-пароля")
    def login(self, username, password):
        self._element(self.INPUT_LOGIN).clear()
        self._element(self.INPUT_LOGIN).send_keys(username)
        self._element(self.INPUT_PASSWORD).clear()
        self._element(self.INPUT_PASSWORD).send_keys(password)
        self._element(self.LOGIN_BUTTON).click()
        