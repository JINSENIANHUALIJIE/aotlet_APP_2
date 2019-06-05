from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    username_edit_text = By.ID, "com.yunmall.lc:id/logon_account_textview"

    password_edit_text = By.ID, "com.yunmall.lc:id/logon_password_textview"

    login_button = By.ID, "com.yunmall.lc:id/logon_button"

    def input_username(self, value):
        self.input(self.username_edit_text, value)

    def input_password(self, value):
        self.input(self.password_edit_text, value)

    def click_login(self):
        self.click(self.login_button)
