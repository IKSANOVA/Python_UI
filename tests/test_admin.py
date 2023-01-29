from page_objects.AdminPage import AdminPage
import allure
import pytest
import pytest_failed_screenshot

url = "https://demo-opencart.ru/admin/"


@allure.suite("Страница администратора")
@allure.title("Проверка отображения элементов")
@pytest.mark.pytest_failed_screenshot()
def test_admin(browser):
    browser.get(url)
    AdminPage(browser).check_logo()
    AdminPage(browser).check_help_text()
    AdminPage(browser).check_forgot_password()
    AdminPage(browser).check_login_button()
