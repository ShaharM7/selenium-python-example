import os
from distutils.util import strtobool

from selenium.webdriver.chrome.options import Options


class BrowserOptions(Options):
    def __init__(self):
        super().__init__()

        print(strtobool(os.getenv('REMOTEBROWSER_CONFIG_USE_SELENIUM_GRID')))
        use_selenium_grid = bool(strtobool(os.getenv('REMOTEBROWSER_CONFIG_USE_SELENIUM_GRID')))
        if use_selenium_grid:
            self.set_capability('bstack:options', {
                "os": os.getenv('REMOTEBROWSER_CONFIG_OS_NAME'),
                "osVersion": os.getenv('REMOTEBROWSER_CONFIG_OS_VERSION'),
                "browserName": os.getenv('REMOTEBROWSER_CONFIG_BROWSER_NAME'),
                "browserVersion": os.getenv('REMOTEBROWSER_CONFIG_BROWSER_VERSION')
            })

        arguments = os.environ.get("BROWSER_OPTIONS_CONFIG_ARGUMENTS").split(",")
        for argument in arguments:
            self.add_argument(argument)
