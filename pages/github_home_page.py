from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from drivers.awaiter import Awaiter
from pages.abstract_page import AbstractPage
from pages.sign_in_page import SignInPage


class GitHubHomePage(AbstractPage):
    SIGN_IN_BUTTON = (By.XPATH, "//a[normalize-space()='Sign in']")

    def __init__(self, browser, awaiter: Awaiter, sign_in_page: SignInPage):
        super().__init__(browser, awaiter)
        self.sign_in_page = sign_in_page

    def sign_in(self) -> SignInPage:
        self.awaiter.until(expected_conditions.element_to_be_clickable(self.SIGN_IN_BUTTON)).click()
        return self.sign_in_page
