#!/usr/bin/env python
# encoding: utf-8
"""
@author: mayuyang
@time: 2020/8/17 13:55
@desc:
"""

from pages.base.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class LoginPage(BasePage):
    _username_input = (By.ID,'user_name')
    _pwd_input = (By.ID,'password')
    _login_button = (By.ID,'confirm')
    _login_name_text = (By.XPATH,"//div[@class='fl']/a[1]")
    _quit_login_button = (By.XPATH, '//*[text()="退出登录"]')

    def write_username(self,content):
        username_input = self.find(self._username_input)
        self.write(username_input,content)

    def write_pwd(self,content):
        pwd_input = self.find(self._pwd_input)
        self.write(pwd_input,content)

    def click_login_button(self):
        login_button = self.find(self._login_button)
        self.click(login_button)

    def login(self,username=None,pwd=None):
        self.write_username(username)
        self.write_pwd(pwd)
        self.click_login_button()

    def get_header_text(self):
        return self.get_text(self.find(self._login_name_text))

    def quit_login(self):
        self.click(self.find(self._quit_login_button))


if __name__ == "__main__":
    l = LoginPage("https://m-stage.dongfangfuli.com/user/login?city=145",type="H5")
    l.login("18721705015","123456")
    time.sleep(10)
    # print(l.get_header_text())
