from dotenv import load_dotenv
import os
from .base_page import BasePage
from playwright.sync_api import expect
from utils.logger_config import setup_logger

# Load environment variables
load_dotenv()
BASE_URL = os.getenv('BASE_URL')

# Setting up the logger
logger = setup_logger()

class HomePage(BasePage):
    """
    This class represents the Home Page and provides methods to interact with
    its elements and verify navigation-related actions.
    """

    # Selectors
    MANAGE_TO_DO_ITEMS_BUTTON = '//button[contains(text(),"Manage To-Do Items")]'
    MANAGE_FOLDERS_BUTTON = "//button[contains(text(),'Manage Folders')]"

    def click_on_manage_to_do_items_button(self):
        """
        Clicks the 'Manage To-Do Items' button to navigate to the corresponding section.
        Logs the action.
        """
        logger.info("Clicking on the 'Manage To-Do Items' button.")
        self.page.wait_for_load_state('load')
        self.click(self.MANAGE_TO_DO_ITEMS_BUTTON)
        logger.info("'Manage To-Do Items' button clicked.")

    def click_on_manage_folders_button(self):
        """
        Clicks the 'Manage Folders' button to navigate to the folders section.
        Logs the action.
        """
        logger.info("Clicking on the 'Manage Folders' button.")
        self.page.wait_for_load_state('load')
        self.click(self.MANAGE_FOLDERS_BUTTON)
        logger.info("'Manage Folders' button clicked.")

    def verify_home_message(self):
        """
        Verifies the presence of the home page welcome message indicating the user is logged in.
        Logs the verification process.
        """
        logger.info("Verifying the home page message for user login.")
        self.page.wait_for_load_state('load')
        expect(self.page.get_by_text('You are logged in as "user"')).to_be_visible()
        logger.info("Home page login message verified successfully.")

    def verify_redirection_to_home_page(self):
        """
        Verifies that the current URL matches the home page URL.
        Logs the verification process.
        """
        logger.info("Verifying redirection to the home page.")
        self.page.wait_for_load_state('load')
        expect(self.page).to_have_url(f"{BASE_URL}/")
        logger.info("Successfully redirected to the home page.")
