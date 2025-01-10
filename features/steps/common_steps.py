import os
import pytest
from pytest_bdd import given, when, then, parsers
from dotenv import load_dotenv
from pages.login_page import LoginPage
from pages.folders_page import FoldersPage
from pages.components.top_bar_component import TopBarComponent

load_dotenv()
BASE_URL = os.getenv('BASE_URL')
USERNAME = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

@pytest.fixture(scope="function")
def login_page(page):
    return LoginPage(page)

@pytest.fixture(scope="function")
def top_bar_component(page):
    return TopBarComponent(page)

@pytest.fixture(scope="function")
def folders_page(page):
    return FoldersPage(page)

@given('the user is on the login page')
def step_given(login_page):
    login_page.navigate(BASE_URL)
    

@when('the user enters valid credentials')
def step_when(login_page):
    login_page.enters_credentials(USERNAME, PASSWORD)
    
@when('the user clicks on the Sign In button')
def step_when(login_page):
    login_page.click_on_sign_in_button()

@given('the user is logged in')
def step_given(login_page):
    login_page.navigate(BASE_URL)
    login_page.enters_credentials(USERNAME, PASSWORD)
    login_page.click_on_sign_in_button()

@when('the user clicks on the Manage Folders button')
def step_when(home_page):
    home_page.click_on_manage_folders_button()


@when('the user clicks on the Create new Folder button')
def step_when(folders_page):
    folders_page.click_on_create_new_folder_button()

@when(parsers.parse('the user enters the folder name "{folder_name}"'))
def step_when(folders_page, folder_name):
    folders_page.fill_name_field(folder_name)
   
@when('the user clicks the Save button')
def step_when(folders_page):
    folders_page.click_on_save_button()

@then('a message is displayed confirming the deletion')
def step_then(folders_page):
    folders_page.verify_pop_up_confirmation()

@when('the user clicks on the Account button')
def step_when(top_bar_component):
    top_bar_component.click_on_account_menu()