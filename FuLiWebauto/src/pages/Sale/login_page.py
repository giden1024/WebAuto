#!usr/bin/env python
#-*- coding:utf -*-
'''
@author = 'mayuyang'
@file:learn_loop_2.py
@time:2019/4/244:51 PM
@desc:
'''
from pages.RedCommon.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    _username_input = (By.XPATH,'//*[@class="el-form"]/div[1]/div/div/input')
    _pwd_input = (By.XPATH,'//*[@class="el-form"]/div[2]/div/div/input')
    _login_button = (By.XPATH,'//*[@class="submit"]/button')
    _header_text = (By.XPATH,'//*[@class="el-header"]/header')

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
        return self.get_text(self.find(self._header_text))


if __name__ == "__main__":
    l = LoginPage()
    l.login("18721700000","123456")
