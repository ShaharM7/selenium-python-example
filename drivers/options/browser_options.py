import os
from distutils.util import strtobool

from selenium.webdriver.chrome.options import Options


class BrowserOptions(Options):
    def __init__(self):
        super().__init__()

        arguments = os.environ.get("BROWSER_OPTIONS_CONFIG_ARGUMENTS").split(",")
        for argument in arguments:
            self.add_argument(argument)

        use_selenium_grid = bool(strtobool(os.getenv('REMOTEBROWSER_CONFIG_USE_SELENIUM_GRID')))
        if use_selenium_grid:
            self.set_capability('os', os.getenv('REMOTEBROWSER_CONFIG_OS_NAME'))
            self.set_capability('os_version', os.getenv('REMOTEBROWSER_CONFIG_OS_VERSION'))
            self.set_capability('browser_name', os.getenv('REMOTEBROWSER_CONFIG_BROWSER_NAME'))
            self.set_capability('browser_version', os.getenv('REMOTEBROWSER_CONFIG_BROWSER_VERSION'))

            browser_stack_options = {'user_name': os.getenv('REMOTEBROWSER_CONFIG_BROWSERSTACKOPTIONS_USERNAME'),
                                     'access_key': os.getenv('REMOTEBROWSER_CONFIG_BROWSERSTACKOPTIONS_ACCESSKEY')}
            self.set_capability('bstack:options', browser_stack_options)
