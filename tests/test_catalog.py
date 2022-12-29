from page_objects.CatalogPage import CatalogPage


url = "https://demo-opencart.ru/index.php?route=product/category&path=20"


def test_check_catalog(browser):
    browser.get(url)
    CatalogPage(browser).check_list_group()
    CatalogPage(browser).check_label()
    CatalogPage(browser).check_sort()
    CatalogPage(browser).check_list()
