import pytest
from locators.auth_locators import AuthLocators
from pages.signup_and_login_page import SignupAndLoginPage

class TestSignupAndLogin:
    login_email = None

    def test_signup(self, driver, base_url):
        driver.get(base_url)

        signup_and_login_page = SignupAndLoginPage(driver)

        # Click on the Register button to go to the signup page
        signup_and_login_page.click_login_button()
        signup_and_login_page.click_register_button()

        # Fill in the signup form with valid data
        
        name = "Test User"
        email = signup_and_login_page.real_time_data_generator()
        TestSignupAndLogin.login_email = email  # Store the generated email for later use in the login test
        password = "Test@123"
        confirm_password = "Test@123"

        signup_and_login_page.fill_signup_form(name, email, password, confirm_password)

        # Click on the Create Account button
        signup_and_login_page.click_create_account_button()

        email_locate = signup_and_login_page.email_locate() 
         # Wait for the email element to be visible
        assert email_locate.text == f"User [{email}]", f"Expected '{email}' not found on page"

    def test_login(self, driver, base_url):
        driver.get(base_url)

        signup_and_login_page = SignupAndLoginPage(driver)

        # Click on the Login button to go to the login page
        signup_and_login_page.click_login_button()

        # Fill in the login form with valid credentials
        email = self.login_email
        assert email, "Expected the generated email from signup to be available for login"
        password = "Test@123"

        signup_and_login_page.fill_login_form(email, password)

        # Click on the Login Submit button
        signup_and_login_page.click_login_submit_button()

        # assertions to verify successful login, such as checking for a specific element that appears after login

        assert "https://a.testable.io" in driver.current_url, "Login failed, expected URL to contain 'https://a.testable.io'"