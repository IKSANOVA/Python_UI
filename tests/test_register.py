from page_objects.RegisterPage import RegisterPage


url = "https://demo-opencart.ru/index.php?route=account/register"


def test_check_register(browser):
    browser.get(url)
    RegisterPage(browser).check_firstname()
    RegisterPage(browser).check_lastname()
    RegisterPage(browser).check_email()
    RegisterPage(browser).check_telephon()
