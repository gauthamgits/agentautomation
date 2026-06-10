# Framework Guide

## Stack
- UI testing: Playwright (sync API) + pytest
- API testing: requests via BaseAPIClient
- Test runner: pytest

## Fixtures available in conftest.py
- `page` — Playwright Page object, function-scoped
- `api_client` — BaseAPIClient instance, session-scoped
- `base_url` — the app's base URL as a string

## Writing UI tests
- Create a page object by subclassing BasePage from tests/pages/base_page.py
- Pass `page` and `base_url` as constructor arguments
- Use self.navigate("/path"), self.click(), self.fill(), self.get_text(), self.is_visible()
- Save page objects to tests/pages/<feature>_page.py

## Writing API tests
- Create a service by subclassing BaseAPIClient from tests/services/base_api_client.py
- Use self.get(), self.post()
- Save service clients to tests/services/<feature>_service.py

## Test file location
- Always save generated tests to tests/stories/<STORY-KEY>/test_<feature>.py

## Test function naming
- test_<action>_<expected_outcome>
- Example: test_login_with_valid_credentials_redirects_to_dashboard
- Example: test_login_with_invalid_credentials_shows_error_message

## Assertions
- Use plain assert statements
- Assert on visible outcomes: page titles, error messages, URLs, response fields