from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from drivers.awaiter import Awaiter
from pages.abstract_page import AbstractPage


class SignInPage(AbstractPage):
    USER_NAME_INPUTBOX = (By.ID, "login_field")
    PASSWORD_INPUTBOX = (By.ID, "password")
    SIGN_IN_BUTTON = (By.NAME, 'commit')
    ERROR_MESSAGE_TEXT = (By.CSS_SELECTOR, "div[role='alert']")

    def __init__(self, browser, awaiter: Awaiter):
        super().__init__(browser, awaiter)

    def enter_user_name(self, user_name: str) -> None:
        self.awaiter.until(EC.element_to_be_clickable(self.USER_NAME_INPUTBOX)).send_keys(user_name)

    def enter_password(self, password: str) -> None:
        self.awaiter.until(EC.element_to_be_clickable(self.PASSWORD_INPUTBOX)).send_keys(password)

    def click_sign_in(self) -> None:
        self.awaiter.until(EC.element_to_be_clickable(self.SIGN_IN_BUTTON)).click()

    def get_error_incorrect_message(self) -> str:
        error_message_element = self.awaiter.until(EC.visibility_of_element_located(self.ERROR_MESSAGE_TEXT))
        return error_message_element.text.strip()
