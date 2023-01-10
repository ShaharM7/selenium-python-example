from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class Awaiter(WebDriverWait):
    def __init__(self, browser: WebDriver, config):
        super().__init__(browser, timeout=config.awaiter_config.timeout)
        self.driver = browser
        self.timeout = config.awaiter_config.timeout
        self.poll_frequency = config.awaiter_config.polling_interval
        self.driver.implicitly_wait(config.awaiter_config.implicit_wait)
        self.driver.set_script_timeout(config.awaiter_config.asynchronous_java_script)
        self.driver.set_page_load_timeout(config.awaiter_config.page_load)


