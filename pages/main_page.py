from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
import math
class MainPage(BasePage): 
    def go_to_login_page(self):
        #login_link = self.browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        login_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        login_link.click()  
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    # def book_name(self):
        # #login_link = self.browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        # book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        # a = book_name.text
        # print(a)  
    def korzina(self):
        #login_link = self.browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        korzina = self.browser.find_element(*ProductPageLocators.KORZINA)
        print("Попали сюда")
        korzina.click()      
    def book_namek(self):   
        #book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        #a = book_name.text 
        #print(a)        
        book_namek = self.browser.find_element(*ProductPageLocators.BOOK_NAMEK).text
        #b = book_namek.text        
        #print(b)
        assert "Coders at Work" == book_namek, 'Название товара не совпадает'
    def cena_tovara(self):      
        cena_tovara = self.browser.find_element(*ProductPageLocators.CENA_TOVARA).text
        print("Попали сюда1", cena_tovara)
        assert "£19.99" == cena_tovara, 'Стоимость корзины не совпадает с ценой товара'    
                
        # book_name = self.browser.find_element(...)
        # a = book_name.text
        # book_name_in_basket = self.browser.find_element(...)
        # b = book_name_in_basket.text
        # assert a == b, 'Название товара не совпадает'