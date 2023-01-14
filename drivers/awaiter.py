import os

from selenium.webdriver.support.wait import WebDriverWait


class Awaiter(WebDriverWait):
    def __init__(self, browser):
        super().__init__(browser, timeout=float(os.environ.get('AWAITER_CONFIG_TIMEOUT')))
        self.driver = browser
        self.timeout = float(os.environ.get('AWAITER_CONFIG_TIMEOUT'))

        self.driver.implicitly_wait(float(os.environ.get('AWAITER_CONFIG_IMPLICIT_WAIT')))
        self.driver.set_script_timeout(float(os.environ.get('AWAITER_CONFIG_ASYNCHRONOUS_JAVA_SCRIPT')))
        self.driver.set_page_load_timeout(float(os.environ.get('AWAITER_CONFIG_PAGE_LOAD')))
