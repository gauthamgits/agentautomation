import pytest
from tests.pages.login_practice_page import LoginPracticePage


def test_login_with_valid_credentials_navigates_to_homepage(page, base_url):
    login_page = LoginPracticePage(page, base_url)
    login_page.navigate_to_login()
    
    login_page.login(
        username="rahulshettyacademy",
        password="Learning@830$3mK2)",
        accept_terms=True
    )
    
    page.wait_for_url("**/shop", timeout=10000)
    assert "shop" in page.url


def test_login_with_incorrect_credentials_shows_error_message(page, base_url):
    login_page = LoginPracticePage(page, base_url)
    login_page.navigate_to_login()
    
    login_page.login(
        username="incorrect_user",
        password="incorrect_password",
        accept_terms=True
    )
    
    page.wait_for_selector(login_page.error_message, state="visible", timeout=5000)
    assert login_page.is_error_message_visible()
    error_text = login_page.get_error_message()
    assert "Incorrect username/password." in error_text
