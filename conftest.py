import os.path

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--url", default="https://demo-opencart.ru"
    )
    parser.addoption(
        "--driver", default="Chrome"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def driver(request):
    str_driver = request.config.getoption("--driver")
    if str_driver == "Chrome":
        driver = webdriver.Chrome(executable_path=os.path.expanduser("C:/driver/chromedriver"))
    elif str_driver == "FireFox":
        driver = webdriver.Chrome(executable_path=os.path.expanduser("C:/driver/geckodriver"))
    elif str_driver == "Opera":
        driver = webdriver.Chrome(executable_path=os.path.expanduser("C:/driver/operadriver"))
    else:
        raise ValueError(f"Incorrect driver {str_driver}")

    yield driver

    driver.close()