from page_objects.MainPage import MainPage
import allure

url = "https://demo-opencart.ru/"

@allure.suite("Главная страница")
@allure.title("Проверка отображения элементов")
def test_check_main(browser):
    browser.get(url)
    MainPage(browser).check_title()
    MainPage(browser).check_search()
    MainPage(browser).check_h3()
    MainPage(browser).check_button()
    MainPage(browser).check_click_button()
