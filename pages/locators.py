from selenium.webdriver.common.by import By

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    KORZINA = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    BOOK_NAMEK = (By.CSS_SELECTOR, "#basket_formset > div > div > div.col-sm-4 > h3 > a")
    CENA_TOVARA = (By.CSS_SELECTOR, "#basket_formset > div > div > div.col-sm-1 > p")
    