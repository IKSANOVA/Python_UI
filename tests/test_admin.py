from page_objects.AdminPage import AdminPage


url = "https://demo-opencart.ru/admin/"


def test_admin(browser):
    browser.get(url)
    AdminPage(browser).check_logo()
    AdminPage(browser).check_help_text()
    AdminPage(browser).check_forgot_password()
    AdminPage(browser).check_login_button()
