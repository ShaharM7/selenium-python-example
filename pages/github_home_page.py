class GitHubHomePage(object):

    def __init__(self, browser, awaiter):
        super.__init__(browser, awaiter)
        self.browser = browser
        self.awaiter = awaiter

    def navigate_to_home_page(self):
        self.browser.get("https://github.com/")
        self.awaiter.until(lambda browser: browser.find_element_by_css_selector("body"))
