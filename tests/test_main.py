from page_objects.MainPage import MainPage


url = "https://demo-opencart.ru/"


def test_check_main(browser):
    browser.get(url)
    MainPage(browser).check_title()
    MainPage(browser).check_search()
    MainPage(browser).check_h3()
    MainPage(browser).check_button()
    MainPage(browser).check_click_button()
    

