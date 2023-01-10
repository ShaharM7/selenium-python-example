from pages.github_home_page import GitHubHomePage


class PageNavigator(object):
    def __init__(self, browser, git_hub_home_page: GitHubHomePage, config):
        self.browser = browser
        self.git_hub_home_page = git_hub_home_page

        self.base_url = config.navigation_config.baseurl

    def navigate_to_git_hub_home_page(self) -> GitHubHomePage:
        self.browser.get(self.base_url)
        return self.git_hub_home_page
