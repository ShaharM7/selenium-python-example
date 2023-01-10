from webdriver_manager.driver import ChromeDriver

from p_automation.drivers.options.browser_options import BrowserOptions


class ChromeBrowser(ChromeDriver):
    def __int__(self, chrome_options: BrowserOptions, config):
        super.__init__(chrome_options)
        self.config = config
