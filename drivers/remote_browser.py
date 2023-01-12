import os

from selenium import webdriver


class RemoteBrowser(webdriver.Remote):
    def __init__(self, options):
        command_executor = os.getenv('REMOTEBROWSER_CONFIG_SELENIUM_GRID_URL')
        capabilities = options.to_capabilities()
        super().__init__(command_executor=command_executor, desired_capabilities=capabilities)
