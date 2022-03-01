import pytest
import time
import math    
from .pages.main_page import MainPage
from selenium.webdriver.common.by import By
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()
    page.go_to_login_page() 
    time.sleep(2)    
    page.solve_quiz_and_get_code()
    #page.book_name()
    time.sleep(10) 
    page.korzina()
    time.sleep(10)    
    page.book_namek()
    time.sleep(10)
    page.cena_tovara()
    time.sleep(10)
