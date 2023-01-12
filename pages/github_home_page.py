from pages.abstract_page import AbstractPage


class GitHubHomePage(AbstractPage):

    def __init__(self, browser, awaiter):
        super.__init__(browser, awaiter)
        self.browser = browser
        self.awaiter = awaiter
