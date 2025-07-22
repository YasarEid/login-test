from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver, timeout=10):
        # Set up driver and wait time
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def visit(self, url):
        # Open the given URL
        self.driver.get(url)

    def find(self, locator):
        # Wait for element to be visible, then return it
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        # Wait for element to be clickable, then click it
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def fill(self, locator, value):
        # Find input, clear it, then type value
        element = self.find(locator)
        element.clear()
        element.send_keys(value)

    def is_visible(self, locator):
        # Check if element is visible, return True or False
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
