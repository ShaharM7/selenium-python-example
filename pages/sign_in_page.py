from abc import ABC

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from drivers.awaiter import Awaiter
from pages.abstract_page import AbstractPage

USER_NAME_INPUTBOX_ID = "login_field"
PASSWORD_INPUTBOX_ID = "password"
SIGN_IN_BUTTON_NAME = 'commit'


class SignInPage(AbstractPage):
    def __init__(self, browser, awaiter: Awaiter):
        super.__init__(browser, awaiter)
        self.browser = browser
        self.awaiter = awaiter

    def enter_user_name(self, user_name: str) -> None:
        self.awaiter.until(EC.element_to_be_clickable(By.ID, USER_NAME_INPUTBOX_ID)).send_keys(user_name)

    def enter_password(self, password: str) -> None:
        self.awaiter.until(EC.element_to_be_clickable(By.ID, PASSWORD_INPUTBOX_ID)).send_keys(password)

    def click_sign_in(self) -> None:
        self.awaiter.until(EC.element_to_be_clickable(By.NAME, SIGN_IN_BUTTON_NAME)).click()
