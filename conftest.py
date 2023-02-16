import os.path

import pytest
from selenium import webdriver
import logging
import datetime
import allure


def pytest_addoption(parser):
    parser.addoption("--api_url", default="https://jsonplaceholder.typicode.com")
    parser.addoption("--opencart_url", default="https://demo.opencart.com")
    parser.addoption("--browser", default="chrome")
    parser.addoption("--browser_version", action="store", default="107.0")
    parser.addoption("--executor",
                     # имя контейнера в сети selenoid
                     default="selenoid",
                     )
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--video", action="store_true", default=False)

@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")
    
    
@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    browser_version = request.config.getoption("--browser_version")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    video = request.config.getoption("--video")
    base_url = request.config.getoption("--opencart_url")

    driver = webdriver.Remote(
        command_executor=f"http://{executor}:4444/wd/hub",
        desired_capabilities={
            "browserName": browser,
            "browserVersion": browser_version,
            "selenoid:options": {
                "enableVNC": vnc,
                "enableVideo": video
            }
        }
    )

    driver.close()
    logger.info("Test {} finished at {}".format(request.node.name, datetime.datetime.now()))
