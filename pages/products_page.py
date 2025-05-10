from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def sort_by_price_low_to_high(self):
        Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container")).select_by_value("lohi")

    def add_lowest_priced_items_to_cart(self):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        for item in items[:2]:
            item.find_element(By.TAG_NAME, "button").click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
