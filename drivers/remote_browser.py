from selenium import webdriver


class RemoteBrowser(webdriver.Remote):
    def __init__(self, config, browser_options):
        command_executor = config.remote_browser_config.selenium_grid_url
        capabilities = browser_options.to_capabilities()
        super().__init__(command_executor=command_executor, desired_capabilities=capabilities)
