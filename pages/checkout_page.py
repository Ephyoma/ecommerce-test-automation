from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_user_info(self, first, last, postal):
        self.wait.until(EC.presence_of_element_located((By.ID, "first-name")))
        self.driver.find_element(By.ID, "first-name").send_keys(first)
        self.driver.find_element(By.ID, "last-name").send_keys(last)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal)
        self.driver.find_element(By.ID, "continue").click()

    def get_summary_prices(self):
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_info")))
        item_prices = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        subtotal = sum(float(p.text.replace("$", "")) for p in item_prices)
        tax = float(self.driver.find_element(By.CLASS_NAME, "summary_tax_label").text.replace("Tax: $", ""))
        total = float(self.driver.find_element(By.CLASS_NAME, "summary_total_label").text.replace("Total: $", ""))
        return subtotal, tax, total

    def finish_checkout(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()
