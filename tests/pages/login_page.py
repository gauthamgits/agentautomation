from tests.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page, base_url):
        super().__init__(page, base_url)
        self.username_input = "#username"
        self.password_input = "#password"
        self.terms_checkbox = "#terms"
        self.signin_button = "#signInBtn"
        self.error_message = ".alert"
        self.page_title = ".navbar-brand"

    def navigate_to_login(self, url):
        self.page.goto(url)

    def enter_username(self, username):
        self.fill(self.username_input, username)

    def enter_password(self, password):
        self.fill(self.password_input, password)

    def select_terms_checkbox(self):
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
            self.select_terms_checkbox()
        self.click_signin()

    def get_current_url(self):
        return self.page.url
