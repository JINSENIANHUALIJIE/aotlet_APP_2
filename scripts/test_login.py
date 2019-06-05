import time

from base.base_driver import init_driver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
    def test_login(self):
        #首页点击我
        self.page.home.click_me()
        #我界面点击已有账号去登陆
        self.page.register.click_login()
        #登陆界面输入用户名
        self.page.login.input_username("itheima_test")
        #登陆界面输入密码
        self.page.login.input_password("itheima")
        #登陆界面点击登陆
        self.page.login.click_login()

        time.sleep(2)
        assert self.driver.current_activity != "/com.yunmall.ymctoc.ui.activity.MainActivity"


