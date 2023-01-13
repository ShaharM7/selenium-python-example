import os

from selenium import webdriver


class RemoteBrowser(webdriver.Remote):
    def __init__(self, options):
        command_executor = str(os.getenv('REMOTEBROWSER_CONFIG_SELENIUM_GRID_URL'))
        super().__init__(command_executor=command_executor, options=options)
