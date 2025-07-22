from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import os

class LoginPage(BasePage):
    # Locators for elements on the login page
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.ID, "submit")
    ERROR_MESSAGE = (By.ID, "error")
    HEADER = (By.XPATH, "//h2[text()='Test login']")

    @property
    def LOGIN_URL(self):
        # Get login URL from environment variable
        return f"{os.getenv('BASE_URL')}/practice-test-login"

    def load(self):
        # Open login page and check it loaded
        self.visit(self.LOGIN_URL)
        assert self.is_loaded(), "Login page did not load properly."

    def login(self, username, password):
        # Fill username and password, then click submit
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)

    def is_loaded(self):
        # Check if page header is visible
        return self.is_visible(self.HEADER)

    def get_error_message(self):
        # Get text from error message element
        return self.find(self.ERROR_MESSAGE).text
