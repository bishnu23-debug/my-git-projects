from selenium.webdriver.common.by import By

class AuthLocators:
    # Signup Locators
    LOGIN_BUTTON = (By.XPATH, "//a[@href='https://a.testable.io']")
    REGISTER_BUTTON = (By.ID, "ember4")
    SIGNUP_NAME = (By.ID, "signupName")
    SIGNUP_EMAIL = (By.ID, "signupEmail")
    SIGNUP_PASSWORD = (By.ID, "signupPassword")
    SIGNUP_CONFIRM_PASSWORD = (By.XPATH, "//input[@placeholder='Confirm Password']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[@type='submit']")
    EMAIL_LOCATE = (By.XPATH, f"//li[contains(@class, 'navbar-user')]//span[contains(text, '')]")

    # Login Locators
    LOGIN_EMAIL = (By.ID, "email")
    LOGIN_PASSWORD = (By.ID, "password")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
