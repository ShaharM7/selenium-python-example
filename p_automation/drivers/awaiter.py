from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from config import AWAITERCONFIG_TIMEOUT, AWAITERCONFIG_POLLINGINTERVAL, AWAITERCONFIG_IMPLICITWAIT, \
    AWAITERCONFIG_ASYNCHRONOUSJAVASCRIPT, AWAITERCONFIG_PAGELOAD


class Awaiter(WebDriverWait):
    def __init__(self, driver: WebDriver, timeout: float = AWAITERCONFIG_TIMEOUT):
        super().__init__(driver, timeout)
        self.driver = driver
        self.timeout = AWAITERCONFIG_TIMEOUT
        self.poll_frequency = AWAITERCONFIG_POLLINGINTERVAL
        self.driver.implicitly_wait(AWAITERCONFIG_IMPLICITWAIT)
        self.driver.set_script_timeout(AWAITERCONFIG_ASYNCHRONOUSJAVASCRIPT)
        self.driver.set_page_load_timeout(AWAITERCONFIG_PAGELOAD)
