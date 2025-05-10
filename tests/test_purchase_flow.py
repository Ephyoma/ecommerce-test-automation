import time
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage

def test_complete_purchase_flow(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url

    products = ProductsPage(driver)
    products.sort_by_price_low_to_high()
    products.add_lowest_priced_items_to_cart()
    products.go_to_cart()

    cart = CartPage(driver)
    items = cart.get_cart_items()
    assert len(items) == 2
    cart.click_checkout()

    checkout = CheckoutPage(driver)
    checkout.enter_user_info("Test", "User", "12345")
    subtotal, tax, total = checkout.get_summary_prices()
    assert subtotal > 0 and total > 0
    checkout.finish_checkout()

    confirm = ConfirmationPage(driver)
    confirm.capture_screenshot()
    assert confirm.is_order_successful()
    
