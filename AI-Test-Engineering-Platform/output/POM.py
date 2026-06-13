from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = self.setup_logger()

        self.username_field = (MobileBy.ACCESSIBILITY_ID, "username")
        self.password_field = (MobileBy.ACCESSIBILITY_ID, "password")
        self.login_button = (MobileBy.ACCESSIBILITY_ID, "loginButton")
        self.error_message = (MobileBy.ACCESSIBILITY_ID, "errorMessage")

    def setup_logger(self):
        logger = logging.getLogger("LoginPage")
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler("appium_test.log")
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def enter_username(self, username):
        self.logger.info("Entering username")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_field)).send_keys(username)

    def enter_password(self, password):
        self.logger.info("Entering password")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_field)).send_keys(password)

    def click_login_button(self):
        self.logger.info("Clicking login button")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button)).click()

    def get_error_message(self):
        self.logger.info("Retrieving error message if present")
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.error_message)).text

    def validate_login(self, username, password, expected_error=None):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

        if expected_error:
            error = self.get_error_message()
            assert expected_error in error, f"Expected error message: '{expected_error}', but got: '{error}'"
        else:
            self.logger.info("Login successful, expected to navigate to the home screen")  
            # Additional logic to validate successful login can be added here

    def clear_fields(self):
        self.logger.info("Clearing input fields")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_field)).clear()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_field)).clear()