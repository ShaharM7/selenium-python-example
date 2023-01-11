import pytest

from containers import Container
from drivers.awaiter import Awaiter
from drivers.options.browser_options import BrowserOptions
from drivers.remote_browser import RemoteBrowser
from navigation.page_navigator import PageNavigator
from pages.github_home_page import GitHubHomePage


@pytest.fixture
def container():
    container = Container()

    config = container.config()

    var = config.get_json_files()[0]
    print(var)

    browser_options = BrowserOptions(config)
    # chrome_browser = ChromeBrowser(browser_options)
    browser = RemoteBrowser(config, browser_options)
    awaiter = Awaiter(browser, config)
    github_home_page = GitHubHomePage(browser, awaiter)
    page_navigator = PageNavigator(browser, github_home_page, config)

    return container


def test_git_hub_home_page(container):
    browser = container.page_navigator
