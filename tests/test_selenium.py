from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_default(driver, base_url):
    driver.get(base_url)
    wait = WebDriverWait(driver, 2)
    wait.until(EC.title_is("Your Store"))
    wait.until(EC.visibility_of_element_located((By.NAME, "search")))
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3")))
    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#search > span > button"))
    )
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#cart > button")))


def test_catalog(driver, base_url):
    driver.get(base_url + "/index.php?route=product/category&path=20")
    wait = WebDriverWait(driver, 2)
    wait.until(EC.title_is("Desktops"))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "list-group")))
    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div.col-md-4.col-xs-6 > div > label")
        )
    )
    wait.until(EC.visibility_of_element_located((By.ID, "input-sort")))
    wait.until(EC.visibility_of_element_located((By.ID, "list-view")))


def test_register(driver, base_url):
    driver.get(base_url + "/index.php?route=account/register")
    wait = WebDriverWait(driver, 2)
    wait.until(EC.visibility_of_element_located((By.ID, "input-firstname")))
    wait.until(EC.visibility_of_element_located((By.NAME, "newsletter")))
    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input.btn.btn-primary"))
    )
    wait.until(EC.invisibility_of_element_located((By.NAME, "customer_group_id")))
    wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/form/div/div/a'))
    ).click()


def test_admin(driver, base_url):
    driver.get(base_url + "/admin/")
    wait = WebDriverWait(driver, 2)
    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div.panel-heading > h1 > i")
        )
    )
    wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.text-right > button")))


def test_product(driver, base_url):
    driver.get(base_url + "/index.php?route=product/product&path=20&product_id=40")
    wait = WebDriverWait(driver, 2)
    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-child(1) > a > img"))
    )
    wait.until(EC.visibility_of_element_located((By.ID, "button-cart")))
    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div.btn-group > button:nth-child(1)")
        )
    )
    wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "ul.nav.nav-tabs > li:nth-child(2) > a")
        )
    )
    wait.until(EC.visibility_of_element_located((By.NAME, "quantity")))
