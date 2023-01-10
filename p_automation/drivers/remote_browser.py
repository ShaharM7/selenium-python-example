from selenium.webdriver.remote.webdriver import WebDriver


class RemoteBrowser(WebDriver):
    def __int__(self, chrome_options):
        self.chrome_options = chrome_options


