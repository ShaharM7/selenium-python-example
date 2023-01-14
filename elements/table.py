from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from elements.abstract_element import AbstractElement


class Table(AbstractElement):
    TOTAL_ROWS = (By.TAG_NAME, "tr")

    def __init__(self, browser, awaiter, element):
        super().__init__(browser=browser, awaiter=awaiter, base_element=element)

    def get_total_rows(self):
        self.awaiter.until(expected_conditions.visibility_of_all_elements_located(self.TOTAL_ROWS))
