import pytest
from playwright.sync_api import sync_playwright
from config.settings import Settings
from tests.services.base_api_client import BaseAPIClient

settings = Settings()

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=settings.headless)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(base_url=settings.base_url)
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="session")
def api_client():
    return BaseAPIClient(
        base_url=settings.api_base_url,
        token=settings.api_token
    )

@pytest.fixture(scope="session")
def base_url():
    return settings.base_url