import os

from pages.github_home_page import GitHubHomePage


class PageNavigator(object):
    def __init__(self, browser, github_home_page: GitHubHomePage):
        self.browser = browser
        self.github_home_page = github_home_page

    def navigate_to_home_page(self) -> GitHubHomePage:
        self.browser.get(os.getenv('NAVIGATION_CONFIG_BASEURL'))
        return self.github_home_page
