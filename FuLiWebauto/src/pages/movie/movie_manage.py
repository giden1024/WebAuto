#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2021/1/28 9:52 
# @Author : mayuyang
# @File : movie_manage.py
import time

from selenium.webdriver.common.by import By
from pages.base.base_page import BasePage

class MovieMange(BasePage):
    supply = "时光网"
    _account_login = (By.ID, "account_login_tab")
    _username_input = (By.ID, "login_account")
    _pwd_input = (By.ID, "login_password")
    _captcha_input = (By.ID, "login_verify")
    _login_submit = (By.ID, "df-submit")
    _manage_lab = (By.XPATH, '//*[@lay-tips="电影管理"]')
    _third_lab = (By.XPATH, '//a[text()="三方供应商管理"]')
    _supply_input = (By.XPATH, "//*[@class='layui-fluid']/div/div/div/div[3]/div[1]/div[1]/select")
    _choose_otion = (By.XPATH, '//*[@class="test-table-reload-btn"]/div[1]/div/dl/dd[text()="%s"]'%supply)
    _related_input = (By.XPATH, "//*[@class='layui-fluid']/div/div/div/div[3]/div[1]/div[5]")
    _related_option = (By.XPATH, '//*[@class="test-table-reload-btn"]/div[5]/div/dl/dd[text()="未关联"]')
    _movie_name_input = (By.ID,"name")
    _search_submit = (By.ID, "searchbt")

    def login(self,username,pwd,captcha=None):
        self.click(self.find(self._account_login))
        # 登录账号密码
        self.write(self.find(self._username_input),username)
        self.write(self.find(self._pwd_input),pwd)
        # self.write(self.find(self._captcha_input),captcha)
        time.sleep(10)
        self.click(self.find(self._login_submit))

    def third_cinema(self,movie_name):
        self.click(self.find(self._manage_lab))
        self.click(self.find(self._third_lab))
        time.sleep(3)
        self.click(self.find(self._supply_input))
        self.write(self.find(self._movie_name_input),movie_name)
        self.click(self.find(self._search_submit))



    def third_movie(self):
        pass

    def third_schedule(self):
        pass

if __name__ == "__main__":
    m = MovieMange("http://10.8.110.68:18091/")
    m.login("admin","123456")
    m.third_cinema("敦化九州国际影城")