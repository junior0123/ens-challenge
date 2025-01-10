import os
import pytest
from pytest_bdd import when, then, scenarios, parsers
from .common_steps import *

from pages.home_page import HomePage
from pages.account_settings_page import AccountPageSettings
from pages.folders_page import FoldersPage
from pages.components.top_bar_component import TopBarComponent
scenarios(os.path.join(os.path.dirname(__file__), '../scenarios/account_settings.feature'))


@pytest.fixture(scope="function")
def home_page(page):
    return HomePage(page)

@pytest.fixture(scope="function")
def top_bar_component(page):
    return TopBarComponent(page)

@pytest.fixture(scope="function")
def account_settings_page(page):
    return AccountPageSettings(page)

@when('the user selects the Settings option')
def step_when(top_bar_component):
    top_bar_component.click_on_settings_button()
    
@when(parsers.parse('the user updates the first name to "{name}"'))
def step_when(account_settings_page, name):
    account_settings_page.fill_name(name)
    
@when(parsers.parse('the user updates the last name to "{last_name}"'))
def step_when(account_settings_page, last_name):
    account_settings_page.fill_description(last_name)
    
@when(parsers.parse('the user updates the email to "{email}"'))
def step_when(account_settings_page, email):
    
    account_settings_page.fill_email(email)

@when('the user clicks the save button')
def step_when(account_settings_page):
    account_settings_page.click_on_save_button()
    
@then('the user sees a confirmation pop-up indicating the changes have been saved')
def step_then(account_settings_page):
    account_settings_page.verify_pop_up_confirmation()

