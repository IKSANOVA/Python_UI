from page_objects.AdminPage import AdminPage


url = "https://demo-opencart.ru/admin/"


# def test_add_new_product(browser):
#     r_device_name = 'test'
#     browser.get(url)
#     AdminPage(browser).login_with("admin", "admin")
#     AdminPage(browser).click_catalog()
#     AdminPage(browser).click_products()
#     AdminPage(browser).click_add_new()
#     AdminPage(browser).new_device_check(r_device_name, "test2", "test3", r_device_name)
#     assert AdminPage(browser).search_element(r_device_name) == r_device_name


# def test_del_product(browser):
#     browser.get(url)
#     AdminPage(browser).login_with("admin", "admin")
#     AdminPage(browser).click_catalog()
#     AdminPage(browser).click_products()
#     deleted_device = AdminPage(browser).first_device()
#     AdminPage(browser).delete_device()
#     new_device = AdminPage(browser).first_device()
#     assert new_device != deleted_device


def test_admin(browser):
    browser.get(url)
    AdminPage(browser).check_logo()
    AdminPage(browser).check_help_text()
    AdminPage(browser).check_forgot_password()
    AdminPage(browser).check_login_button()

