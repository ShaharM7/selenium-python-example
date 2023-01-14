import os

from selenium.webdriver.chrome.options import Options

from utils.convert import str2bool


class BrowserOptions(Options):
    def __init__(self):
        super().__init__()

        arguments = str(os.getenv("BROWSER_OPTIONS_CONFIG_ARGUMENTS")).split(",")
        for argument in arguments:
            print(argument)
            self.add_argument(str(argument))

        use_selenium_grid = str2bool(os.getenv('REMOTEBROWSER_CONFIG_USE_SELENIUM_GRID'))
        if use_selenium_grid:
            self.set_capability('bstack:options', {
                "os": os.getenv('REMOTEBROWSER_CONFIG_OS_NAME'),
                "osVersion": os.getenv('REMOTEBROWSER_CONFIG_OS_VERSION'),
                "browserName": os.getenv('REMOTEBROWSER_CONFIG_BROWSER_NAME'),
                "browserVersion": os.getenv('REMOTEBROWSER_CONFIG_BROWSER_VERSION')
            })
