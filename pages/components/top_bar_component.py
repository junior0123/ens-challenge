from dotenv import load_dotenv
from ..base_page import BasePage
import os
from utils.logger_config import setup_logger
from playwright.sync_api import expect

# Load environment variables
load_dotenv()
BASE_URL = os.getenv('BASE_URL')

# Setting up the logger
logger = setup_logger()

class TopBarComponent(BasePage):
    """
    Represents the top bar component of the website, providing methods for interacting
    with various elements in the top bar.
    """

    # Selectors for top bar elements
    ACCOUNT_MENU = "#account-menu"
    DROP_DOWN_SETTINGS_BUTTON = 'a[data-cy="settings"]'
    DROP_DOWN_LOGOUT_BUTTON = 'a[data-cy="logout"]'
    HOME_BUTTON = '.d-flex.align-items-center.nav-link.active'

    def click_on_account_menu(self):
        """
        Clicks on the 'Account Menu' button in the top bar to open a dropdown menu.
        Logs the action and waits for the modal to be visible.
        """
        logger.info("Attempting to click on the 'Account Menu' button.")
        self.page.wait_for_load_state('load')
        self.click(self.ACCOUNT_MENU)
        logger.info("'Account Menu' dropdown opened successfully.")

    def click_on_logout_button(self):
        """
        Clicks on the 'Logout' option in the dropdown menu to log out the user.
        Logs the action and verifies that the logout message is displayed.
        """
        logger.info("Attempting to click on the 'Logout' option.")
        self.page.wait_for_load_state('load')
        self.click(self.DROP_DOWN_LOGOUT_BUTTON)
        
        logger.info("Verifying 'Logged out successfully!' message is visible.")
        expect(self.page.get_by_role("heading", name="Logged out successfully!")).to_be_visible()
        logger.info("Logout confirmed.")

    def click_on_settings_button(self):
        """
        Clicks on the 'Settings' option in the dropdown menu.
        Logs the action.
        """
        logger.info("Attempting to click on the 'Settings' button in the dropdown menu.")
        self.page.wait_for_load_state('load')
        self.click(self.DROP_DOWN_SETTINGS_BUTTON)
        logger.info("'Settings' button clicked.")

    def verify_logged_out_message(self):
        """
        Verifies that the 'Logged out successfully!' message is visible.
        Logs the verification process.
        """
        logger.info("Verifying the 'Logged out successfully!' message.")
        self.page.wait_for_load_state('load')
        expect(self.page.get_by_role("heading", name="Logged out successfully!")).to_be_visible()
        logger.info("'Logged out successfully!' message verified.")

    def verify_session_is_terminated(self):
        """
        Verifies that the user session has been terminated by checking the URL.
        Logs the verification process.
        """
        logger.info("Verifying the session has been terminated.")
        self.page.wait_for_load_state('load')
        expect(self.page).to_have_url(f"{BASE_URL}/logout")
        logger.info("Session termination confirmed.")

    def click_on_home_button(self):
        """
        Clicks on the 'Home' button in the top bar.
        Logs the action.
        """
        logger.info("Attempting to click on the 'Home' button.")
        self.page.wait_for_load_state('load')
        self.click(self.HOME_BUTTON)
        logger.info("'Home' button clicked.")
