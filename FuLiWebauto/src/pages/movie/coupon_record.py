#!/usr/bin/env python
# encoding: utf-8
"""
@author: mayuyang
@time: 2020/8/17 14:02
@desc:
"""
import time

from selenium.webdriver.common.by import By
from pages.B.login_page import LoginPage


class CouponRecord(LoginPage):

    _record_link = (By.XPATH, '//*[@class="content editor"]/div/div[8]')
    _record_title = (By.XPATH, '//*[@class="clearfix"]/span')
    _record_line = (By.XPATH, '//*[@class="el-card__body"]/div/div[3]/table/tbody/tr')

    def to_record(self):
        self.click(self.find(self._record_link))
        self.my_wait(5,self._record_title,"券记录")

    def get_record_line_info(self,line=1):
        coupon_list = []
        for x in range(1,8):
            coupon_list.append(self.get_text(self.find((By.XPATH, '//*[@class="el-card__body"]/div'
                                                                  '/div[3]/table/tbody/tr[%s]/td[%s]/div' % (line,x)))))
        return coupon_list

    def get_record_line(self): # 获取首页的数据一共多少行
        return len(self.findall(self._record_line))


class SearchRecord(CouponRecord):
    _write_off_search = (By.XPATH, '//*[@class="el-row"]/div/div/div/div/div/input')
    _write_off_option_yes = (By.XPATH, '//*[@class="el-scrollbar"]/div/ul/li/span[text()="已核销"]')
    _write_off_option_no = (By.XPATH, '//*[@class="el-scrollbar"]/div/ul/li/span[text()="未核销"]')
    _search_button = (By.XPATH, '//*[@class="el-row"]/div[2]/div/div/div/button[1]')

    def search_status(self,write_status):
        self.click(self.find(self._write_off_search))
        if write_status == "已核销":
            self.click(self.find(self._write_off_option_yes))
        elif write_status == "未核销":
            self.click(self.find(self._write_off_option_no))
        self.click(self.find(self._search_button))

    def get_search_result(self):
        flag = True
        for x in range(self.get_record_line()):
            print(x)
            if self.get_record_line_info(x+1)[-2:] != ['','']:
                flag = False
                print(x)
        return flag


class ViewRecord(CouponRecord):
    _view_button = (By.XPATH, '')

    def to_view(self,line):
        self.click(self.find((By.XPATH, '//*[@class="el-card__body"]/div/div[3]/'
                                        'table/tbody/tr[%s]/td[8]/div/button' % line)))

    def get_view_page_info(self):
        time.sleep(5)
        page_info = []
        for x in range(1,11):
            page_info.append(self.get_text(self.find((By.XPATH, '//*[@class="el-form coupon-form"]/div[%d]/div' % x))))
        return page_info

    def test_find(self):
        for x in range(1,11):
            self.find((By.XPATH, '//*[@class="el-form coupon-form"]/div[1]/div'))


if __name__ == "__main__":
    c = ViewRecord("http://vrs.uat1.rs.com/b/#/login")
    c.login("18721705015","123456")
    c.to_record()
    c.to_view(1)
    print(c.get_view_page_info())

