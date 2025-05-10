import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage

def test_locked_out_user_cannot_login(driver):
    login = LoginPage(driver)
    login.load()
    login.login("locked_out_user", "secret_sauce")

    error = login.driver.find_element("css selector", "[data-test='error']").text
    assert "locked out" in error.lower()
