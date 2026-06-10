from tests.pages.base_page import BasePage


class LoginPracticePage(BasePage):
    def __init__(self, page, base_url):
        super().__init__(page, base_url)
        self.username_input = "#username"
        self.password_input = "#password"
        self.terms_checkbox = "#terms"
        self.signin_button = "#signInBtn"
        self.error_message = "[style*='block'] .alert-danger"
        
    def navigate_to_login(self):
        self.page.goto("https://rahulshettyacademy.com/loginpagePractise")
        
    def enter_username(self, username):
        self.fill(self.username_input, username)
        
    def enter_password(self, password):
        self.fill(self.password_input, password)
        
    def check_terms_and_conditions(self):
        self.click(self.terms_checkbox)
        
    def click_signin(self):
        self.click(self.signin_button)
        
    def get_error_message(self):
        return self.get_text(self.error_message)
        
    def is_error_message_visible(self):
        return self.is_visible(self.error_message)
        
    def login(self, username, password, accept_terms=True):
        self.enter_username(username)
        self.enter_password(password)
        if accept_terms:
            self.check_terms_and_conditions()
        self.click_signin()
