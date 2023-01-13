from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from drivers.awaiter import Awaiter
from pages.abstract_page import AbstractPage
from pages.sign_in_page import SignInPage

SIGN_IN_BUTTON_XPATH = "//a[normalize-space()='Sign in']"


class GitHubHomePage(AbstractPage):
    def __init__(self, browser, awaiter: Awaiter, sign_in_page: SignInPage):
        super().__init__(browser, awaiter)
        self.sign_in_page = sign_in_page

    def sign_in(self) -> SignInPage:
        self.awaiter.until(EC.element_to_be_clickable((By.XPATH, SIGN_IN_BUTTON_XPATH))).click()
        return self.sign_in_page
