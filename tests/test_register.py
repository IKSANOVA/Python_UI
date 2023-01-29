from page_objects.RegisterPage import RegisterPage
import allure

url = "https://demo-opencart.ru/index.php?route=account/register"


@allure.suite("Страница регистрации")
@allure.title("Проверка отображения элементов")
def test_check_register(browser):
    browser.get(url)
    RegisterPage(browser).check_firstname()
    RegisterPage(browser).check_lastname()
    RegisterPage(browser).check_email()
    RegisterPage(browser).check_telephon()
