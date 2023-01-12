import os

import pytest
from dotenv import load_dotenv

from drivers.awaiter import Awaiter
from drivers.chrome_browser import ChromeBrowser
from drivers.options.browser_options import BrowserOptions
from drivers.remote_browser import RemoteBrowser


@pytest.fixture
def set_up():

    load_dotenv()
    options = BrowserOptions()
    if os.getenv('REMOTEBROWSER_CONFIG_USE_SELENIUM_GRID') is True:
        browser = RemoteBrowser(options=options)
    else:
        browser = ChromeBrowser(options=options)
    awaiter = Awaiter(browser)

    return browser, awaiter


def test_github_home_page(set_up):
    pass
