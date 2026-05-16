import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = "https://testable.io/enterprise"  


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def driver():

    chrome_options = Options()

    chrome_options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        },
    )

    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-features=PasswordCheck")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    yield driver

    driver.quit()