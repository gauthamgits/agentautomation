from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def navigate(self, path: str = ""):
        self.page.goto(f"{self.base_url}{path}")

    def click(self, selector: str):
        self.page.locator(selector).click()

    def fill(self, selector: str, value: str):
        self.page.locator(selector).fill(value)

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text()

    def is_visible(self, selector: str, timeout: int = 5000) -> bool:
        try:
            self.page.locator(selector).wait_for(state="visible", timeout=timeout)
            return True
        except:
            return False

    def wait_for_url(self, pattern: str):
        self.page.wait_for_url(f"**{pattern}**")