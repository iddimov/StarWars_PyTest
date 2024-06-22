import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright):
    browser = playwright.chromium.launch()
    yield browser
    browser.close()

@pytest.fixture(scope="session")
def base_url():
    return "https://swapi.dev/api"