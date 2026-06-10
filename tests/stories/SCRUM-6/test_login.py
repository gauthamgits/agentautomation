import pytest
from tests.pages.login_practice_page import LoginPracticePage


class TestLogin:
    
    @pytest.fixture(autouse=True)
    def setup(self, page, base_url):
        self.login_page = LoginPracticePage(page, base_url)
        self.page = page
        
    def test_login_with_valid_credentials_navigates_to_homepage(self):
        """
        AC1: Given the test endpoint, valid username and password,
        when I try to login with the provided credentials and select terms checkbox,
        then I should be able to login successfully and be navigated to the homepage.
        """
        self.login_page.navigate_to_login()
        self.login_page.login(
            username="rahulshettyacademy",
            password="Learning@830$3mK2)",
            accept_terms=True
        )
        
        self.page.wait_for_url("**/angularpractice/shop", timeout=10000)
        
        assert "shop" in self.page.url, "User should be navigated to homepage after successful login"
        
    def test_login_with_incorrect_credentials_shows_error_message(self):
        """
        AC2: Given the test endpoint,
        when I try to login with incorrect username and password and select terms checkbox,
        then I should see an error message: "Incorrect username/password."
        """
        self.login_page.navigate_to_login()
        self.login_page.login(
            username="invaliduser",
            password="invalidpassword",
            accept_terms=True
        )
        
        self.page.wait_for_selector(self.login_page.error_message, timeout=5000)
        
        assert self.login_page.is_error_message_visible(), "Error message should be visible"
        
        error_text = self.login_page.get_error_message()
        assert "Incorrect username/password." in error_text, f"Expected error message not found. Got: {error_text}"
