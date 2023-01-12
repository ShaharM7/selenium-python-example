import os

from selenium.webdriver.chrome.options import Options


class BrowserOptions(Options):
    def __init__(self):
        super().__init__()

        for argument in os.getenv('BROWSER_OPTIONS_CONFIG_ARGUMENTS'):
            self.add_argument(argument)

        if os.getenv('REMOTEBROWSER_CONFIG_USE_SELENIUM_GRID'):
            self.set_capability('os', os.getenv('REMOTEBROWSER_CONFIG_OS_NAME'))
            self.set_capability('os_version', os.getenv('REMOTEBROWSER_CONFIG_OS_VERSION'))
            self.set_capability('browser_name', os.getenv('REMOTEBROWSER_CONFIG_BROWSER_NAME'))
            self.set_capability('browser_version', os.getenv('REMOTEBROWSER_CONFIG_BROWSER_VERSION'))
            self.set_capability('bstack:options', '')
