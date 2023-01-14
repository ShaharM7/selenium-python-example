import abc

from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions


class AbstractElement(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, browser, awaiter, base_element):
        self.browser = browser
        self.awaiter = awaiter
        self.element = base_element

    def click(self):
        el = self.awaiter.until(expected_conditions.element_to_be_clickable(self.element))
        self._highlight_element(el, "green")
        el.click()

    def fill_text(self, txt):
        el = self.awaiter.until(expected_conditions.element_to_be_clickable(self.element))
        el.clear()
        self._highlight_element(el, "green")
        el.send_keys(txt)

    def clear_text(self):
        el = self.awaiter.until(expected_conditions.element_to_be_clickable(self.element))
        el.clear()

    def scroll_to_bottom(self):
        self.awaiter.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def submit(self):
        self._highlight_element(self.element, "green")
        self.element.submit()

    def get_text(self):
        el = self.awaiter.until(expected_conditions.visibility_of_element_located(self.element))
        self._highlight_element(el, "green")
        return el.text

    def move_to_element(self):
        action = ActionChains(self.browser)
        self.awaiter.until(expected_conditions.visibility_of(self.element))
        action.move_to_element(self.element).perform()

    def is_elem_displayed(self):
        try:
            return self.element.is_displayed()
        except StaleElementReferenceException:
            return False
        except NoSuchElementException:
            return False

    def _highlight_element(self, color):
        original_style = self.element.get_attribute("style")
        new_style = f"background-color:yellow;border: 1px solid {color}{original_style}"
        self.browser.execute_script(
            "var tmpArguments = arguments;setTimeout(function () {tmpArguments[0].setAttribute('style', '"
            + new_style + "');},0);", self.element)
        self.browser.execute_script(
            "var tmpArguments = arguments;setTimeout(function () {tmpArguments[0].setAttribute('style', '"
            + original_style + "');},400);", self.element)
