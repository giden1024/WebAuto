#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2021/1/28 9:52 
# @Author : mayuyang
# @File : movie_job.py
import time

from selenium.webdriver.common.by import By
from pages.base.base_page import BasePage

class MovieJob(BasePage):


    _login_username = (By.NAME,"userName")
    _login_pwd = (By.NAME,"password")
    _login_button = (By.XPATH,'//*[@class="row"]/div[2]/button')
    _job_info_desc = (By.ID,"jobDesc")
    _job_execute_button = (By.XPATH,'//*[text()="执行"]')
    _execute_param = (By.NAME, "executorParam")
    _execute_save = (By.XPATH, '//*[@class="modal fade in"]/div/div/div[2]/form/div[2]/div/button[1]')

    def login(self,username,pwd):
        username_input = self.find(self._login_username)
        self.write(username_input,username)
        pwd_input = self.find(self._login_pwd)
        self.write(pwd_input,pwd)
        login_button = self.find(self._login_button)
        self.click(login_button)


    def execute_job(self,url,job_name,job_info_text=None):
        self.goto_url(url)
        time.sleep(1)

        job_desc_input = self.find(self._job_info_desc)
        self.write(job_desc_input,job_name)
        job_execute_button = self.find(self._job_execute_button)
        self.click(job_execute_button)
        if job_info_text != None:
            self.write(self.find(self._execute_param),job_info_text)
        self.click(self.find(self._execute_save))


if __name__ == "__main__":
    m = MovieJob("http://10.8.109.11:12017/")
    m.login("admin","123456")
    url = "http://10.8.109.11:12017/jobinfo?jobGroup=85"
    m.execute_job(url,"时光影院同步")
    print(1)
    m.execute_job(url, "时光影片同步")
    print(2)
