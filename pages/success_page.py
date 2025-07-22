from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import os

class SuccessPage(BasePage):
    # Locators for elements on success page
    TITLE = (By.XPATH, "//div[@class='post-header']//h1[contains(text(), 'Logged In Successfully')]")
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Log out']")
    CONFIRMATION_MESSAGE = (By.XPATH, "//p[contains(text(), 'Congratulations')]")

    @property
    def SUCCESS_URL(self):
        # URL for success page from env variable
        return f"{os.getenv('BASE_URL')}/logged-in-successfully"

    def load(self):
        # Open the success page URL
        self.visit(self.SUCCESS_URL)

    def is_loaded(self):
        # Check if title and logout button are visible
        return self.is_visible(self.TITLE) and self.is_visible(self.LOGOUT_BUTTON)

    def logout(self):
        # Click the logout button
        self.click(self.LOGOUT_BUTTON)
