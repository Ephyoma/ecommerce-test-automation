from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def get_cart_items(self):
        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        return [(item.find_element(By.CLASS_NAME, "inventory_item_name").text,
                 float(item.find_element(By.CLASS_NAME, "inventory_item_price").text.replace("$", "")))
                for item in items]

    def click_checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
