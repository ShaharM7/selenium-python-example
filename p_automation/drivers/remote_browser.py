from selenium import webdriver


class RemoteBrowser(webdriver.Remote):
    def __int__(self, config, browser_options):
        super(self).__int__(command_executor=config.remote_browser_config.selenium_grid_url,
                            browser_options=browser_options)
        self.browser_options = browser_options
        # browser_options.set_capability("browserVersion", "67")
        # browser_options.set_capability("platformName", "Windows XP")
