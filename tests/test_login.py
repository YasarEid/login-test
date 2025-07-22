from pages.login_page import LoginPage
from pages.success_page import SuccessPage
import test_data

def test_valid_login(driver):
    """Test that a user can log in with valid credentials."""
    # Step 1: Login
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(test_data.VALID_USERNAME, test_data.VALID_PASSWORD)
    success_page = SuccessPage(driver)
    assert success_page.is_loaded(), "Success page not loaded."

def test_invalid_username(driver):
    """Test that login fails with an invalid username."""
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(test_data.INVALID_USERNAME, test_data.VALID_PASSWORD)
    assert login_page.get_error_message() == test_data.ERROR_MSG_INVALID_USERNAME

def test_invalid_password(driver):
    """Test that login fails with an invalid password."""
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(test_data.VALID_USERNAME, test_data.INVALID_PASSWORD)
    assert login_page.get_error_message() == test_data.ERROR_MSG_INVALID_PASSWORD

def test_protected_page_without_login(driver):
    """Test that the protected page is not accessible without logging in."""
    success_page = SuccessPage(driver)
    success_page.load()
    assert not success_page.is_loaded(), "ERROR: Protected page is accessible without login."

def test_access_after_logout(driver):
    """Verify that after logging out, the user cannot access the protected page."""
    # Step 1: Login
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(test_data.VALID_USERNAME, test_data.VALID_PASSWORD)

    success_page = SuccessPage(driver)
    assert success_page.is_loaded()

    # Step 2: Logout
    success_page.logout()
    assert login_page.is_loaded()

    # Step 3: Try to access protected page again
    success_page.load()
    assert not success_page.is_loaded(), "ERROR: Protected page is accessible after logout."
