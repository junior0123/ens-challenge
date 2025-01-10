import os
import pytest
from pytest_bdd import when, then, scenarios, parsers
from .common_steps import *
from pages.home_page import HomePage
from pages.to_do_items_page import ToDoItemsPage
from pages.folders_page import FoldersPage
from pages.components.top_bar_component import TopBarComponent
scenarios(os.path.join(os.path.dirname(__file__), '../scenarios/to_do_items.feature'))


@pytest.fixture(scope="function")
def home_page(page):
    return HomePage(page)

@pytest.fixture(scope="function")
def top_bar_component(page):
    return TopBarComponent(page)

@pytest.fixture(scope="function")
def to_do_items(page):
    return ToDoItemsPage(page)

@pytest.fixture(scope="function")
def folders_page(page):
    return FoldersPage(page)

@when('the user clicks on the Manage To-Do Items button')
def step_when(home_page):
    home_page.click_on_manage_to_do_items_button()

@then('the user sees the option to create a new to do item')
def step_then(to_do_items):
    to_do_items.verify_visibility_create_to_do_item_button()

@then('the user is redirected to the Manage To-Do Items page')
def step_then(to_do_items):
    to_do_items.verify_header_message()
    
@when('the user clicks on the Home button')
def step_given(top_bar_component):
    top_bar_component.click_on_home_button()
    
@when('the user clicks on the Create new To-Do Item button')
def step_when(to_do_items):
    to_do_items.click_on_create_new_to_do_item_button()

@when(parsers.parse('the user enters the title "{title}" in the title field'))
def step_when(to_do_items, title):
    to_do_items.fill_title_field(title)
    
@when(parsers.parse('the user enters the description "{description}" in the description field'))
def step_when(to_do_items, description):
    to_do_items.fill_description_field(description)
    
@when(parsers.parse('the user saves the folders id of "{folder_name}" folder'))
def step_given(folders_page, to_do_items, folder_name):
    to_do_items.set_folder_id(folders_page.get_id_folder(folder_name))
    
@when(parsers.parse('the user selects the folder "{string}" for the to-do item'))
def step_when(to_do_items, string):
    to_do_items.select_folder(to_do_items.get_folder_id())
    
@then(parsers.parse('the to-do item "{to_do_item}" appears in the to-do items list'))
def step_then(to_do_items, to_do_item, top_bar_component, home_page, folders_page):
    to_do_items.verify_that_to_do_item_appear_in_the_list(to_do_item)
    to_do_items.click_on_delete_to_do_item(to_do_item)
    to_do_items.click_on_confirm_deletion_button()
    top_bar_component.click_on_home_button()
    home_page.click_on_manage_folders_button()
    folders_page.delete_folder(to_do_items.get_folder_id())
    folders_page.click_on_confirm_deletion_button()
    
@when(parsers.parse('the user clicks on the Delete option of the to do item named "{name}"'))
def step_when(to_do_items, name):
    to_do_items.click_on_delete_to_do_item(name)
    
@when('the user confirms the deletion by clicking the delete button in the popup')
def step_when(to_do_items):
    to_do_items.click_on_confirm_deletion_button()
    to_do_items.verify_pop_up_confirmation()
   
@then(parsers.parse('the to do item named "{name}" no longer appears in the list of to do items'))
def step_then(to_do_items, name, top_bar_component, home_page, folders_page):
    to_do_items.verify_that_to_do_name_does_not_appear_in_the_list(name)
    top_bar_component.click_on_home_button()
    home_page.click_on_manage_folders_button()
    folders_page.delete_folder(to_do_items.get_folder_id())
    folders_page.click_on_confirm_deletion_button()
    
@when(parsers.parse('the user clicks on the edit option of the to do item named "{name}"'))
def step_when(to_do_items, name):
    to_do_items.click_on_edit_to_do_item(name)

@when(parsers.parse('the user updates the title to "{title}"'))
def step_when(to_do_items, title):
    to_do_items.fill_title_field(title)

@when(parsers.parse('the user updates the description to "{description}"'))
def step_when(to_do_items, description):
    to_do_items.fill_description_field(description)

@then(parsers.parse('the to-do item "{name}" no longer appears in the to-do items list'))
def step_then(to_do_items, name):
    to_do_items.verify_that_to_do_name_does_not_appear_in_the_list(name)

@then(parsers.parse('a to-do item named "{name}" appears in the list with the updated data'))
def step_then(to_do_items, name, top_bar_component, home_page, folders_page):
    to_do_items.verify_that_to_do_item_appear_in_the_list(name)
    to_do_items.click_on_delete_to_do_item(name)
    to_do_items.click_on_confirm_deletion_button()
    top_bar_component.click_on_home_button()
    home_page.click_on_manage_folders_button()
    folders_page.delete_folder(to_do_items.get_folder_id())
    folders_page.click_on_confirm_deletion_button()

@then('the user sees a confirmation message indicating the changes were successful')
def step_then(to_do_items):
    to_do_items.verify_pop_up_confirmation()
    