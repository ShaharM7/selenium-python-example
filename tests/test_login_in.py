import os

import pytest
from dotenv import load_dotenv

from drivers.awaiter import Awaiter
from drivers.chrome_browser import ChromeBrowser
from drivers.options.browser_options import BrowserOptions
from drivers.remote_browser import RemoteBrowser
from navigation.page_navigator import PageNavigator
from pages.github_home_page import GitHubHomePage
from pages.sign_in_page import SignInPage
from utils.convert import str2bool


@pytest.fixture
def set_up():
    load_dotenv('../config/.env')

    options = BrowserOptions()
    use_selenium_grid = str2bool(os.getenv('REMOTEBROWSER_CONFIG_USE_SELENIUM_GRID'))
    if use_selenium_grid:
        browser = RemoteBrowser(options=options)
    else:
        browser = ChromeBrowser(options=options)
    awaiter = Awaiter(browser)

    sign_in_page = SignInPage(browser=browser,
                              awaiter=awaiter)

    github_home_page = GitHubHomePage(browser=browser,
                                      awaiter=awaiter,
                                      sign_in_page=sign_in_page)

    page_navigator = PageNavigator(browser=browser,
                                   github_home_page=github_home_page,
                                   sign_in_page=sign_in_page)
    yield page_navigator

    browser.quit()


class TestLoginInPage:
    def test_github_home_page(self, set_up):
        home_page = set_up.navigate_to_home_page()
        sign_in_page = home_page.sign_in()
        sign_in_page.enter_user_name("None")
        sign_in_page.enter_password("None-again")
        sign_in_page.click_sign_in()
        assert "Incorrect username or password.".strip() == sign_in_page.get_error_incorrect_message()
