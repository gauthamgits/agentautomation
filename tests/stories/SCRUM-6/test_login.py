import pytest
from tests.pages.login_page import LoginPage

class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, page, base_url):
        self.page = page
        self.login_page = LoginPage(page, base_url)
        self.test_url = "https://rahulshettyacademy.com/loginpagePractise"

    def test_login_with_valid_credentials_navigates_to_homepage(self):
        self.login_page.navigate_to_login(self.test_url)
        self.login_page.enter_username("rahulshettyacademy")
        self.login_page.enter_password("Learning@830$3mK2)")
        self.login_page.select_terms_checkbox()
        self.login_page.click_signin()

        #self.page.wait_for_timeout(3000)
        current_url = self.login_page.get_current_url()
        assert current_url != self.test_url, f"Expected redirect but stayed on {current_url}"

    def test_login_with_incorrect_credentials_shows_error_message(self):
        self.login_page.navigate_to_login(self.test_url)
        self.login_page.enter_username("incorrectuser")
        self.login_page.enter_password("wrongpassword")
        self.login_page.select_terms_checkbox()
        self.login_page.click_signin()

        # Wait for alert to appear
        self.page.wait_for_selector(".alert", timeout=5000)
        assert self.login_page.is_error_message_visible()
        error_text = self.login_page.get_error_message()
        assert "Incorrect username/password." in error_text
