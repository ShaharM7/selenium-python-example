from webdriver_manager.driver import ChromeDriver


class ChromeBrowser(ChromeDriver):
    def __int__(self, chrome_options):
        super.__init__(chrome_options)
