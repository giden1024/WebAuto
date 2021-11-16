#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2021/10/12 10:39 
# @Author : mayuyang
# @File : create_order.py 
# @desc:


import time,random

from selenium.webdriver.common.by import By
# from pages.base.base_page import BasePage
from pages.user.login_page import LoginPage


# 一些输入金额的页面
class EnterAmount(LoginPage):

    _confirm_button = (By.XPATH, '//*[contains(text(),"确认兑换")]')  # 确认按钮
    _record_line = (By.XPATH, '//*[@class="el-card__body"]/div/div[3]/table/tbody/tr')
    _cash_click_div = (By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div/div[3]/div/div[1]/div[1]/div[3]')
    _cash_submit = (By.XPATH, '//*[contains(text(),"确认抵扣")]')

    def get_pay_url(self, url):
        self.get_url(url)

    def enter_amount(self, amount):
        new_amount = round(random.uniform(0, int(amount)),2)
        # 根据输入的金额点击按键
        for num in str(new_amount):
            _number_span = (By.XPATH, '//span[text()="%s"]' % num)
            time.sleep(1)
            self.click(self.find(_number_span))

        # 点击确认兑换按钮
        self.click(self.find(self._confirm_button))

    #  点击收银台确认页面，然后输入支付密码
    def mcashier_click(self, pwd_key):
        # self.click(self.find(self._cash_click_div))
        time.sleep(1)
        self.click(self.find(self._cash_submit))

        # 点击支付密码
        for num in str(pwd_key):
            _pwd_spant = (By.XPATH, "//ul[@class='pwdKeyBoard___1nQfy']/li/span[text()='%s']" % num)
            self.click(self.find(_pwd_spant))
        time.sleep(1)

    # 购买多次券码
    def buy_code_times(self,times,url,amount,pwd_key):
        for t in range(int(times)):
            self.get_pay_url(url)
            self.enter_amount(amount)
            time.sleep(1)
            self.mcashier_click(pwd_key)


# class SearchRecord(EnterAmount):
#     _write_off_search = (By.XPATH, '//*[@class="el-row"]/div/div/div/div/div/input')
#     _write_off_option_yes = (By.XPATH, '//*[@class="el-scrollbar"]/div/ul/li/span[text()="已核销"]')
#     _write_off_option_no = (By.XPATH, '//*[@class="el-scrollbar"]/div/ul/li/span[text()="未核销"]')
#     _search_button = (By.XPATH, '//*[@class="el-row"]/div[2]/div/div/div/button[1]')
#
#     def search_status(self,write_status):
#         self.click(self.find(self._write_off_search))
#         if write_status == "已核销":
#             self.click(self.find(self._write_off_option_yes))
#         elif write_status == "未核销":
#             self.click(self.find(self._write_off_option_no))
#         self.click(self.find(self._search_button))
#
#     def get_search_result(self):
#         flag = True
#         for x in range(self.get_record_line()):
#             print(x)
#             if self.get_record_line_info(x+1)[-2:] != ['','']:
#                 flag = False
#                 print(x)
#         return flag
#
#
# class ViewRecord(CouponRecord):
#     _view_button = (By.XPATH, '')
#
#     def to_view(self,line):
#         self.click(self.find((By.XPATH, '//*[@class="el-card__body"]/div/div[3]/'
#                                         'table/tbody/tr[%s]/td[8]/div/button' % line)))
#
#     def get_view_page_info(self):
#         time.sleep(5)
#         page_info = []
#         for x in range(1,11):
#             page_info.append(self.get_text(self.find((By.XPATH, '//*[@class="el-form coupon-form"]/div[%d]/div' % x))))
#         return page_info
#
#     def test_find(self):
#         for x in range(1,11):
#             self.find((By.XPATH, '//*[@class="el-form coupon-form"]/div[1]/div'))


if __name__ == "__main__":
    e = EnterAmount("https://m-test05.dongfangfuli.com/user/login?city=145",type="H5")
    e.login("18721705015","123456")
    time.sleep(5)
    url = "https://m-test05.dongfangfuli.com/newBirthday/payBill?id=5405"
    amount = "1"
    pwd_key = "1991"

    e.buy_code_times("8",url,amount,pwd_key)
    # 关闭浏览器
    # e.quit_driver()




