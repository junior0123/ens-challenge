import pytest
from pages.components.top_bar_component import TopBarComponent
from utils.logger_config import setup_logger

# Setting up the logger
logger = setup_logger()

@pytest.fixture(scope="function")
def context(browser):
    """
    Creates a new browser context with specific settings for each test.

    Args:
        browser: The Playwright browser instance.

    Yields:
        context: The Playwright browser context.
    """
    logger.info("Creating a new browser context with custom settings.")
    context = browser.new_context(
        user_agent="custom-agent",  # Custom user agent
        noViewport=True,  # Disabling viewport for full-page rendering
    )
    yield context
    logger.info("Closing the browser context.")
    context.close()

@pytest.fixture(scope="function")
def page(context):
    """
    Creates a new page within the given browser context for each test.

    Args:
        context: The Playwright browser context.

    Yields:
        page: The Playwright page object.
    """
    logger.info("Creating a new page in the browser context.")
    page = context.new_page()
    yield page
    logger.info("Closing the page.")
    page.close()

@pytest.fixture(scope="function")
def top_bar_component(page):
    """
    Initializes the TopBarComponent for interaction with the top bar in tests.

    Args:
        page: The Playwright page object.

    Returns:
        TopBarComponent: An instance of the TopBarComponent class.
    """
    logger.info("Initializing the TopBarComponent.")
    return TopBarComponent(page)

@pytest.hookimpl(tryfirst=True)
def pytest_bdd_after_scenario(request, feature, scenario):
    """
    Pytest-BDD hook executed after each scenario. It handles logout if the scenario is tagged with 'logout'.

    Args:
        request: The pytest request object.
        feature: The feature file being executed.
        scenario: The scenario being executed.
    """
    if "logout" in scenario.tags:
        logger.info(f"Executing logout hook for the scenario: {scenario.name}")
        top_bar_component = request.getfixturevalue('top_bar_component')
        
        logger.info("Clicking on the account menu.")
        top_bar_component.click_on_account_menu()
        
        logger.info("Clicking on the logout button.")
        top_bar_component.click_on_logout_button()
