#!/usr/bin/env python
# encoding: utf-8
"""
@author: mayuyang
@time: 2020/8/1 13:54
@desc:
"""
from pages.RedCommon.base_page import BasePage
from selenium.webdriver.common.by import By


class RegPage(BasePage):
    _reg_name_input = (By.XPATH,'//*[@class="index-container__main"]/form/div[1]/div/div/input')
    _reg_mobile_input = (By.XPATH,'//*[@class="index-container__main"]/form/div[2]/div/div/input')
    _reg_mail_input = (By.XPATH,'//*[@class="index-container__main"]/form/div[3]/div/div/input')
    _reg_submit = (By.XPATH,'//*[@class="index-container__main"]/form/div[4]/div/button')
    _alrt = (By.XPATH,'//*[@role="alert"]/p')
    def reg(self,reg_name,reg_mobile,reg_mail):
        self.write(self.find(self._reg_name_input),reg_name)
        self.write(self.find(self._reg_mobile_input),reg_mobile)
        self.write(self.find(self._reg_mail_input),reg_mail)
        self.click(self.find(self._reg_submit))

        alert_text = self.get_text(self.find(self._alrt))
        print(alert_text)


if __name__ == "__main__":
    r = RegPage("http://vrs.uat1.rs.com/s/#/index")
    r.reg("ceshi","18721700015","124512@qq.com")