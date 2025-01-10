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

class FoldersPage(BasePage):
    """
    This class represents the 'Folders' page, providing methods to interact with folder-related
    actions such as creation, deletion, and verification of folders.
    """

    # Selectors for folder-related actions
    CREATE_NEW_FOLDER_BUTTON = "#jh-create-entity"
    REFRESH_LIST_BUTTON = "//button[contains(., 'Refresh List')]"
    NAME_FIELD = '#folder-name'
    SAVE_BUTTON = '#save-entity'
    CONFIRM_DELETION_BUTTON = '#jhi-confirm-delete-folder'

    def click_on_create_new_folder_button(self):
        """
        Clicks the 'Create New Folder' button.
        Logs the action.
        """
        logger.info("Clicking on the 'Create New Folder' button.")
        self.page.wait_for_load_state('load')
        self.click(self.CREATE_NEW_FOLDER_BUTTON)
        logger.info("'Create New Folder' button clicked.")

    def fill_name_field(self, name):
        """
        Fills the 'Name' field with the provided folder name.
        Logs the action.
        """
        logger.info(f"Filling the 'Name' field with: {name}")
        self.page.wait_for_load_state('load')
        self.page.locator(self.NAME_FIELD).clear()
        self.fill_text(self.NAME_FIELD, name)
        logger.info("'Name' field updated successfully.")

    def click_on_save_button(self):
        """
        Clicks the 'Save' button to save folder changes.
        Verifies the folder list is visible after saving.
        Logs the action.
        """
        logger.info("Clicking on the 'Save' button to save folder changes.")
        self.page.wait_for_load_state('load')
        self.click(self.SAVE_BUTTON)
        self.page.wait_for_selector('table.table').is_visible()
        logger.info("'Save' button clicked, and folder list verified.")

    def verify_visibility_create_new_folder_button(self):
        """
        Verifies that the 'Create New Folder' button is visible.
        Logs the verification process.
        """
        logger.info("Verifying the visibility of the 'Create New Folder' button.")
        self.page.wait_for_load_state('load')
        expect(self.page.get_by_role("link", name="Create new Folder")).to_be_visible()
        logger.info("'Create New Folder' button is visible.")

    def verify_header_message(self):
        """
        Verifies the header message on the folders page.
        Logs the verification process.
        """
        logger.info("Verifying the header message on the 'Folders' page.")
        self.page.wait_for_load_state('load')
        expect(self.page.get_by_role("heading", name="Folders Refresh List   Create")).to_be_visible()
        logger.info("Header message verified.")

    def verify_that_folder_name_appear_in_the_list(self, folder_name):
        """
        Verifies that a folder with the specified name appears in the list.
        Logs the verification process.
        """
        logger.info(f"Verifying that the folder '{folder_name}' appears in the list.")
        self.page.wait_for_load_state('load')
        self.page.wait_for_selector(".table > tbody")
        expect(self.page.locator(f"tr[data-cy='entityTable'] td:has-text('{folder_name}')")).to_be_visible()
        logger.info(f"Folder '{folder_name}' is visible in the list.")

    def verify_that_folder_name_does_not_appear_in_the_list(self, folder_name):
        """
        Verifies that a folder with the specified name does not appear in the list.
        Logs the verification process.
        """
        logger.info(f"Verifying that the folder '{folder_name}' does not appear in the list.")
        self.page.wait_for_load_state('load')
        self.page.wait_for_selector(".table > tbody")
        expect(self.page.locator(f"tr[data-cy='entityTable'] td:has-text('{folder_name}')")).not_to_be_visible()
        logger.info(f"Folder '{folder_name}' is not visible in the list.")

    def delete_folder(self, folder_name):
        """
        Deletes a folder with the specified name by clicking the delete button.
        Logs the action.
        """
        logger.info(f"Attempting to delete the folder: {folder_name}")
        self.page.wait_for_load_state('load')
        self.page.locator(f"//tr[contains(., '{folder_name}')]//a[@data-cy='entityDeleteButton']").click()
        logger.info(f"Delete button for folder '{folder_name}' clicked.")

    def click_on_confirm_deletion_button(self):
        """
        Clicks the confirmation button to finalize folder deletion.
        Logs the action.
        """
        logger.info("Clicking the 'Confirm Deletion' button.")
        self.page.wait_for_load_state('load')
        self.click(self.CONFIRM_DELETION_BUTTON)
        logger.info("'Confirm Deletion' button clicked.")

    def verify_that_the_user_is_on_folders_section(self):
        """
        Verifies that the user is on the 'Folders' section by checking the URL and header.
        Logs the verification process.
        """
        logger.info("Verifying the user is on the 'Folders' section.")
        self.page.wait_for_load_state('load')
        expect(self.page).to_have_url(f"{BASE_URL}/folder")
        expect(self.page.get_by_role("heading", name="Folders Refresh List   Create")).to_be_visible()
        logger.info("User is on the 'Folders' section.")

    def click_on_edit_folder(self, folder_name):
        """
        Clicks the edit button for the specified folder.
        Logs the action.
        """
        logger.info(f"Clicking on the 'Edit' button for folder: {folder_name}")
        self.page.wait_for_load_state('load')
        self.page.locator(f"//tr[contains(., '{folder_name}')]//a[@data-cy='entityEditButton']").click()
        logger.info(f"'Edit' button for folder '{folder_name}' clicked.")

    def verify_pop_up_confirmation(self):
        """
        Verifies the confirmation popup appears after an action.
        Logs the verification process.
        """
        logger.info("Verifying the confirmation popup appears.")
        self.page.wait_for_load_state('load')
        self.page.wait_for_selector(".Toastify__toast-container.Toastify__toast-container--top-left.toastify-container")
        expect(self.page.locator('.Toastify__toast-container.Toastify__toast-container--top-left.toastify-container')).to_be_visible()
        logger.info("Confirmation popup verified.")

    def get_id_folder(self, folder_name):
        """
        Retrieves the ID of a folder by its name.
        Logs the retrieval process.
        """
        logger.info(f"Retrieving ID for folder: {folder_name}")
        self.page.wait_for_load_state('load')
        folder_id = self.page.locator(f"//tr[contains(., '{folder_name}')] //td/a").inner_text()
        logger.info(f"Retrieved ID for folder '{folder_name}': {folder_id}")
        return folder_id
