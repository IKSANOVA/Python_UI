from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class ProductPage(BasePage):
    IMG = (By.CSS_SELECTOR, "li:nth-child(1) > a > img")
    BUY = (By.ID, "button-cart")
    VALUTA = (By.CSS_SELECTOR, "div.btn-group > button:nth-child(1)")
    OTZIV = (By.CSS_SELECTOR, "ul.nav.nav-tabs > li:nth-child(2) > a")
    QANTITY = (By.NAME, "quantity")
    
        
    def check_buy(self):
        self._element(self.BUY)
      
        
    def check_valuta(self):
        self._element(self.VALUTA)
      
        
    def check_otziv(self):
        self._element(self.OTZIV)
      
        
    def check_quantity(self):
        self._element(self.QANTITY)
      
        
    def click_buy(self):
        self._click(self.BUY)
        