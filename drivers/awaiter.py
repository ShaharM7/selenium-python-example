import os

from selenium.webdriver.support.wait import WebDriverWait


class Awaiter(WebDriverWait):
    def __init__(self, browser):
        super().__init__(browser, timeout=float(os.environ.get('AWAITERCONFIG_TIMEOUT')))
        self.driver = browser
        self.timeout = float(os.environ.get('AWAITERCONFIG_TIMEOUT'))
        # self.poll_frequency = AWAITER_CONFIG_POLLING_INTERVAL
        self.driver.implicitly_wait(os.environ.get('AWAITER_CONFIG_IMPLICIT_WAIT'))
        self.driver.set_script_timeout(os.environ.get('AWAITER_CONFIG_ASYNCHRONOUS_JAVA_SCRIPT'))
        self.driver.set_page_load_timeout(os.environ.get('AWAITER_CONFIG_PAGE_LOAD'))
