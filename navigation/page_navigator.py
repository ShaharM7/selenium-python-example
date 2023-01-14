import os

from pages.github_home_page import GitHubHomePage
from pages.sign_in_page import SignInPage


class PageNavigator(object):
    def __init__(self, browser, github_home_page: GitHubHomePage, sign_in_page: SignInPage):
        self.browser = browser
        self.github_home_page = github_home_page
        self.sign_in_page = sign_in_page

    def navigate_to_home_page(self) -> GitHubHomePage:
        self.navigate_to(os.getenv('NAVIGATION_CONFIG_BASEURL'))
        return self.github_home_page

    def navigate_to_sign_in_page(self) -> SignInPage:
        self.navigate_to(os.getenv('NAVIGATION_CONFIG_BASEURL') + os.getenv('NAVIGATION_CONFIG_SIGN_IN_ROUTE'))
        return self.sign_in_page

    def navigate_to(self, url):
        self.browser.get(url)
