from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver
from locators.auth_locators import AuthLocators

class SignupAndLoginPage:
    def __init__(self, driver):
        self.driver = driver

    def real_time_data_generator(self):
        import random
        import string
        email = "testuser" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=1)) + "@yopmail.com"
        return email

    def click_login_button(self):
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(AuthLocators.LOGIN_BUTTON)
        )
        login_button.click()

    def click_register_button(self):
        register_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(AuthLocators.REGISTER_BUTTON)
        )
        register_button.click()

    def fill_signup_form(self, name, email, password, confirm_password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(AuthLocators.SIGNUP_NAME)
        ).send_keys(name)
        self.driver.find_element(*AuthLocators.SIGNUP_EMAIL).send_keys(email)
        self.driver.find_element(*AuthLocators.SIGNUP_PASSWORD).send_keys(password)
        self.driver.find_element(*AuthLocators.SIGNUP_CONFIRM_PASSWORD).send_keys(confirm_password)

    def click_create_account_button(self):
        create_account_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(AuthLocators.CREATE_ACCOUNT_BUTTON)
        )
        create_account_button.click()

    def get_generated_email(self, email):
        email_locator = (AuthLocators.EMAIL_LOCATE[0], AuthLocators.EMAIL_LOCATE[2].format(email=email))
        generated_email_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(email_locator)
        )
        return generated_email_element.text
    
    def email_locate(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(AuthLocators.EMAIL_LOCATE)
        )

    def fill_login_form(self, email, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(AuthLocators.LOGIN_EMAIL)
        ).send_keys(email)
        self.driver.find_element(*AuthLocators.LOGIN_PASSWORD).send_keys(password)

    def click_login_submit_button(self):
        login_submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(AuthLocators.LOGIN_SUBMIT_BUTTON)
        )
        login_submit_button.click()