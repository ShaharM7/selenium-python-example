from selenium.webdriver.chrome.options import Options


class BrowserOptions(Options):
    def __init__(self, config):
        super().__init__()
        for argument in config.browser_options_config.arguments:
            self.add_argument(argument)

        if config.remote_browser_config.use_selenium_grid:
            self.set_capability('browserName', config.remote_browser_config.browser_name)
            self.set_capability('browser_version', config.remote_browser_config.browser_version)
            self.set_capability('bstack:options', config.remote_browser_config.browser_stack_options)
