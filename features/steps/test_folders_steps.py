import os
import pytest
from pytest_bdd import when, then, scenarios, parsers
from .common_steps import *
from pages.home_page import HomePage
from pages.folders_page import FoldersPage
from pages.components.top_bar_component import TopBarComponent
scenarios(os.path.join(os.path.dirname(__file__), '../scenarios/folders.feature'))

@pytest.fixture(scope="function")
def home_page(page):
    return HomePage(page)

@pytest.fixture(scope="function")
def top_bar_component(page):
    return TopBarComponent(page)

@pytest.fixture(scope="function")
def folders_page(page):
    return FoldersPage(page)

@then('the user is redirected to the Manage Folders page')
def step_then(folders_page):
    folders_page.verify_header_message()
@then('the user sees the option to create a Folder')
def step_then(folders_page):
    folders_page.verify_visibility_create_new_folder_button()

@then(parsers.parse('the folder "{folder_name}" appears in the folder list'))
def step_then(folders_page, folder_name):
    folders_page.verify_that_folder_name_appear_in_the_list(folder_name)
    folders_page.delete_folder(folder_name)
    folders_page.click_on_confirm_deletion_button()
    
@when('the user is on the Folders section')
def step_when(folders_page):
    folders_page.verify_that_the_user_is_on_folders_section()

@when(parsers.parse('the user clicks on the Edit option of the folder named "{folder_name}"'))
def step_when(folders_page, folder_name):
    folders_page.click_on_edit_folder(folder_name)
    
@when(parsers.parse('the user enters the new folder name "{folder_name}" in the Name field'))
def step_when(folders_page, folder_name):
    folders_page.fill_name_field(folder_name)

@then(parsers.parse('the folder appears in the list with the new name "{folder_name}"'))
def step_then(folders_page, folder_name):
    folders_page.verify_that_folder_name_appear_in_the_list(folder_name)
    
@then('a popup is displayed with the confirmation of the change')
def step_then(folders_page):
    folders_page.verify_pop_up_confirmation()

@when(parsers.parse('the user clicks on the Delete option of the folder named "{folder_name}"'))
def step_when(folders_page, folder_name):
    folders_page.delete_folder(folder_name)
    
@when('the user confirms the deletion by clicking the Delete button in the popup')
def step_when(folders_page):
    folders_page.click_on_confirm_deletion_button()
    
@then(parsers.parse('the folder named "{folder_name}" no longer appears in the list of folders'))
def step_then(folders_page, folder_name):
    folders_page.verify_that_folder_name_does_not_appear_in_the_list(folder_name)

@then(parsers.parse('the folder updates its name to "{folder_name}"'))
def step_then(folders_page, folder_name):
    folders_page.verify_that_folder_name_appear_in_the_list(folder_name)
    folders_page.delete_folder(folder_name)
    folders_page.click_on_confirm_deletion_button()
    