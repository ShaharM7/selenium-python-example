from selenium import webdriver


class ChromeBrowser(webdriver.Chrome):
    def __init__(self, options):
        super().__init__(desired_capabilities=options.to_capabilities())
