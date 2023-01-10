from pages.abstract_page import AbstractPage


class GitHubHomePage(AbstractPage):
    
    def navigate_to_home_page(self):
        self.browser.get("https://github.com/")
        self.awaiter.until(lambda browser: browser.find_element_by_css_selector("body"))
