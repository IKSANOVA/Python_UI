from page_objects.ProductPage import ProductPage
import allure

url = "https://demo-opencart.ru/index.php?route=product/product&path=20&product_id=40"


@allure.suite("Страница продукта")
@allure.title("Проверка отображения элементов")
def test_check_product(browser):
    browser.get(url)
    ProductPage(browser).check_buy()
    ProductPage(browser).check_otziv()
    ProductPage(browser).check_quantity()
    ProductPage(browser).check_valuta()
    ProductPage(browser).click_buy()
