import os
from .base_page import BasePage
from playwright.sync_api import expect
from utils.logger_config import setup_logger
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
BASE_URL = os.getenv('BASE_URL')

# Setting up the logger
logger = setup_logger()

class LoginPage(BasePage):
    """
    This class represents the login page and provides methods for user authentication actions,
    including filling credentials, submitting the login form, and verifying the page state.
    """

    # Selectors
    USERNAME_FIELD = "#username"
    PASSWORD_FIELD = "#password"
    LOGIN_BUTTON = 'button[type="submit"]'
    CANCEL_BUTTON = 'button[tabindex="1"]'

    def click_on_sign_in_button(self):
        """
        Clicks the login button to submit the form.
        Logs the action for tracking purposes.
        """
        logger.info("Clicking the 'Sign In' button.")
        self.page.wait_for_load_state('load')
        self.click(self.LOGIN_BUTTON)
        logger.info("'Sign In' button clicked successfully.")

    def enters_credentials(self, username: str, password: str):
        """
        Fills in the login form with the provided username and password.
        
        Args:
            username (str): The username for login.
            password (str): The password associated with the username.
        """
        logger.info(f"Entering credentials: username='{username}' and password='******'.")
        self.page.wait_for_load_state('load')
        self.fill_text(self.USERNAME_FIELD, username)
        self.fill_text(self.PASSWORD_FIELD, password)
        logger.info("Credentials entered successfully.")

    def click_on_cancel_button(self):
        """
        Clicks the cancel button to close or exit the login form.
        Logs the action for tracking purposes.
        """
        logger.info("Clicking the 'Cancel' button.")
        self.page.wait_for_load_state('load')
        self.click(self.CANCEL_BUTTON)
        logger.info("'Cancel' button clicked successfully.")

    def navigate(self, url: str):
        """
        Navigates to the specified login page URL.
        
        Args:
            url (str): The URL of the login page to navigate to.
        """
        logger.info(f"Navigating to the login page URL: {url}.")
        super().navigate(url)
        logger.info("Navigation to the login page completed.")

    def verify_error_message(self):
        """
        Verifies the visibility of an error message indicating a failed login attempt.
        Logs the verification process.
        """
        logger.info("Verifying the login error message is visible.")
        self.page.wait_for_load_state('load')
        expect(self.page.get_by_text("Failed to sign in! Please")).to_be_visible()
        logger.info("Error message verified successfully.")

    def verify_the_user_is_on_login_page(self):
        """
        Verifies that the user is on the login page by checking the URL and page heading.
        Logs the verification process.
        """
        logger.info("Verifying the user is on the login page.")
        self.page.wait_for_load_state('load')
        expect(self.page).to_have_url(f"{BASE_URL}/login")
        expect(self.page.get_by_role("heading", name="Sign in")).to_be_visible()
        logger.info("User is confirmed to be on the login page.")
