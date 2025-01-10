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

class ToDoItemsPage(BasePage):
    """
    This class provides methods to interact with the To-Do Items page, such as creating,
    editing, deleting items, and verifying their presence in the list.
    """

    # Selectors
    CREATE_NEW_TO_DO_ITEM_BUTTON = "[data-cy='entityCreateButton']"
    REFRESH_LIST_BUTTON = "//button[contains(., 'Refresh List')]"
    TITLE_FIELD = '#to-do-item-title'
    DESCRIPTION_FIELD = '#to-do-item-description'
    FOLDER_DROP_DOWN = '#to-do-item-folder'
    SAVE_BUTTON = '#save-entity'
    CONFIRM_DELETION_BUTTON = "#jhi-confirm-delete-toDoItem"

    # Attributes
    folder_id = None

    def click_on_create_new_to_do_item_button(self):
        """
        Clicks the 'Create New To-Do Item' button.
        """
        logger.info("Clicking the 'Create New To-Do Item' button.")
        self.page.wait_for_load_state('load')
        self.click(self.CREATE_NEW_TO_DO_ITEM_BUTTON)

    def fill_title_field(self, title):
        """
        Fills the title field with the given text.
        
        Args:
            title (str): The title of the To-Do Item.
        """
        logger.info(f"Filling the title field with: {title}")
        self.page.wait_for_load_state('load')
        self.page.locator(self.TITLE_FIELD).clear()
        self.fill_text(self.TITLE_FIELD, title)

    def fill_description_field(self, description):
        """
        Fills the description field with the given text.
        
        Args:
            description (str): The description of the To-Do Item.
        """
        logger.info(f"Filling the description field with: {description}")
        self.page.wait_for_load_state('load')
        self.page.locator(self.DESCRIPTION_FIELD).clear()
        self.fill_text(self.DESCRIPTION_FIELD, description)

    def select_folder(self, folder):
        """
        Selects a folder from the dropdown menu.
        
        Args:
            folder (str): The folder to select.
        """
        logger.info(f"Selecting the folder: {folder}")
        self.page.wait_for_load_state('load')
        self.click(self.FOLDER_DROP_DOWN)
        self.page.get_by_label("Folder").select_option(folder)

    def click_on_save_button(self):
        """
        Clicks the 'Save' button to save the To-Do Item.
        """
        logger.info("Clicking the 'Save' button.")
        self.page.wait_for_load_state('load')
        self.click(self.SAVE_BUTTON)

    def verify_visibility_create_to_do_item_button(self):
        """
        Verifies that the 'Create New To-Do Item' button is visible.
        """
        logger.info("Verifying visibility of the 'Create New To-Do Item' button.")
        self.page.wait_for_load_state('load')
        expect(self.page.get_by_role("link", name="Create new To Do Item")).to_be_visible()

    def verify_header_message(self):
        """
        Verifies the header message on the To-Do Items page.
        """
        logger.info("Verifying the header message on the To-Do Items page.")
        expect(self.page.get_by_role("heading", name="To Do Items Refresh List")).to_be_visible()

    def set_folder_id(self, folder_id):
        """
        Sets the folder ID attribute.
        
        Args:
            folder_id (str): The ID of the folder to set.
        """
        logger.info(f"Setting folder ID to: {folder_id}")
        self.folder_id = folder_id

    def get_folder_id(self):
        """
        Retrieves the current folder ID.
        
        Returns:
            str: The folder ID.
        """
        logger.info("Retrieving the folder ID.")
        return self.folder_id

    def verify_that_to_do_item_appear_in_the_list(self, to_do_item):
        """
        Verifies that a To-Do Item appears in the list.
        
        Args:
            to_do_item (str): The name of the To-Do Item to verify.
        """
        logger.info(f"Verifying that the To-Do Item '{to_do_item}' appears in the list.")
        self.page.wait_for_load_state('load')
        self.page.wait_for_selector(".table > tbody")
        expect(self.page.locator(f"tr[data-cy='entityTable'] td:has-text('{to_do_item}')")).to_be_visible()

    def click_on_delete_to_do_item(self, to_do_item_name):
        """
        Clicks the delete button for a specific To-Do Item.
        
        Args:
            to_do_item_name (str): The name of the To-Do Item to delete.
        """
        logger.info(f"Clicking delete button for To-Do Item: {to_do_item_name}")
        self.page.wait_for_load_state('load')
        self.page.locator(f"//tr[contains(., '{to_do_item_name}')]//a[@data-cy='entityDeleteButton']").click()

    def click_on_edit_to_do_item(self, to_do_item):
        """
        Clicks the edit button for a specific To-Do Item.
        
        Args:
            to_do_item (str): The name of the To-Do Item to edit.
        """
        logger.info(f"Clicking edit button for To-Do Item: {to_do_item}")
        self.page.wait_for_load_state('load')
        self.page.locator(f"//tr[contains(., '{to_do_item}')]//a[@data-cy='entityEditButton']").click()

    def click_on_confirm_deletion_button(self):
        """
        Clicks the confirmation button to delete a To-Do Item.
        """
        logger.info("Clicking the confirm deletion button.")
        self.page.wait_for_load_state('load')
        self.click(self.CONFIRM_DELETION_BUTTON)

    def verify_pop_up_confirmation(self):
        """
        Verifies the visibility of the pop-up confirmation message.
        """
        logger.info("Verifying the pop-up confirmation message.")
        self.page.wait_for_selector(".Toastify__toast-container.Toastify__toast-container--top-left.toastify-container")
        expect(self.page.locator('.Toastify__toast-container.Toastify__toast-container--top-left.toastify-container')).to_be_visible()

    def verify_that_to_do_name_does_not_appear_in_the_list(self, to_do_name):
        """
        Verifies that a To-Do Item does not appear in the list.
        
        Args:
            to_do_name (str): The name of the To-Do Item to verify its absence.
        """
        logger.info(f"Verifying that the To-Do Item '{to_do_name}' does not appear in the list.")
        self.page.wait_for_selector(".table > tbody")
        expect(self.page.locator(f"tr[data-cy='entityTable'] td:has-text('{to_do_name}')")).not_to_be_visible()
