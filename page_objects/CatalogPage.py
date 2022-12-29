from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage
from selenium.common.exceptions import NoSuchElementException


class CatalogPage(BasePage):
    TITLE = "Desktops"
    GROUP = (By.CLASS_NAME, "list-group")
    LABEL = (By.CSS_SELECTOR, "div.col-md-4.col-xs-6 > div > label")
    SORT = (By.ID, "input-sort")
    LIST = (By.ID, "list-view")

    def check_list_group(self):
        self._element(self.GROUP)

    def check_label(self):
        self._element(self.LABEL)

    def check_sort(self):
        self._element(self.SORT)

    def check_list(self):
        self._element(self.LIST)

    def check_title(self):
        self._check_title(self.TITLE)
