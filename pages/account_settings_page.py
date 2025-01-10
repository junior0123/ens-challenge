from .base_page import BasePage
from playwright.sync_api import expect
from utils.logger_config import setup_logger

# Setting up the logger
logger = setup_logger()

class AccountPageSettings(BasePage):
    """
    This class represents the 'Account Settings' page, providing methods for interacting
    with various elements like name, email fields, and the save button.
    """

    # Selectors for account settings fields and buttons
    FIRST_NAME_FIELD = '#firstName'
    LAST_NAME_FIELD = '#lastName'
    EMAIL_FIELD = '#email'
    SAVE_BUTTON = '[data-cy="submit"]'

    def fill_name(self, name):
        """
        Clears and fills the 'First Name' field with the provided name.
        Logs the action and ensures the page is fully loaded before interacting.
        """
        logger.info(f"Filling the 'First Name' field with: {name}")
        self.page.wait_for_load_state('load')
        self.page.locator(self.FIRST_NAME_FIELD).clear()
        self.fill_text(self.FIRST_NAME_FIELD, name)
        logger.info("'First Name' field updated successfully.")

    def fill_description(self, last_name):
        """
        Clears and fills the 'Last Name' field with the provided last name.
        Logs the action and ensures the page is fully loaded before interacting.
        """
        logger.info(f"Filling the 'Last Name' field with: {last_name}")
        self.page.wait_for_load_state('load')
        self.page.locator(self.LAST_NAME_FIELD).clear()
        self.fill_text(self.LAST_NAME_FIELD, last_name)
        logger.info("'Last Name' field updated successfully.")

    def fill_email(self, email):
        """
        Clears and fills the 'Email' field with the provided email.
        Logs the action and ensures the page is fully loaded before interacting.
        """
        logger.info(f"Filling the 'Email' field with: {email}")
        self.page.wait_for_load_state('load')
        self.page.locator(self.EMAIL_FIELD).clear()
        self.fill_text(self.EMAIL_FIELD, email)
        logger.info("'Email' field updated successfully.")

    def click_on_save_button(self):
        """
        Clicks the 'Save' button to submit the changes.
        Logs the action and ensures the page is fully loaded before interacting.
        """
        logger.info("Clicking on the 'Save' button to submit changes.")
        self.page.wait_for_load_state('load')
        self.click(self.SAVE_BUTTON)
        logger.info("'Save' button clicked successfully.")

    def verify_pop_up_confirmation(self):
        """
        Verifies that the confirmation popup appears after saving changes.
        Logs the verification process and ensures the popup is visible.
        """
        logger.info("Verifying the confirmation popup appears.")
        self.page.wait_for_load_state('load')
        self.page.wait_for_selector(".Toastify__toast-container.Toastify__toast-container--top-left.toastify-container")
        expect(self.page.locator('.Toastify__toast-container.Toastify__toast-container--top-left.toastify-container')).to_be_visible()
        logger.info("Confirmation popup verified successfully.")
