import os
import pytest
from pytest_bdd import when, then, scenarios, parsers
from .common_steps import *
from pages.home_page import HomePage
from pages.components.top_bar_component import TopBarComponent
scenarios(os.path.join(os.path.dirname(__file__), '../scenarios/login.feature'))


@pytest.fixture(scope="function")
def home_page(page):
    return HomePage(page)

@pytest.fixture(scope="function")
def top_bar_component(page):
    return TopBarComponent(page)

@then('the user sees a message saying You are logged in as user')
def step_then(home_page, top_bar_component):
    home_page.verify_home_message()
    top_bar_component.click_on_account_menu()
    top_bar_component.click_on_logout_button()

@then('the user is redirected to the homepage')
def step_then(home_page):
    home_page.verify_redirection_to_home_page()
    
@then('the user sees an error message')
def step_then(login_page):
    login_page.verify_error_message()
    
@then('the user remains on the login page')
def step_then(login_page):
    login_page.verify_the_user_is_on_login_page()
    
@when('the user enters invalid credentials')
def step_when(login_page):
    login_page.enters_credentials("testInvalidUsername", "invalidPassword")

@when('the user clicks on the Sign Out button')
def step_when(top_bar_component):
    top_bar_component.click_on_logout_button()
    
@then('the user sees a confirmation message saying You have been logged out successfully')
def step_then(top_bar_component):
    top_bar_component.verify_logged_out_message()
    
@then('the session is terminated')
def step_then(top_bar_component):
    top_bar_component.verify_session_is_terminated()
   