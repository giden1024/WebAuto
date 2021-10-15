#!/usr/bin/env python
# encoding: utf-8
'''
@author: mayuyang
@time: 2020/6/16 16:26
@desc:
'''
from selenium.webdriver.common.by import By
from pages.Sale.login_page import LoginPage


class OrderPage(LoginPage):
    _shop_page = (By.XPATH,'//*[@class="el-menu"]/a[3]/li')


    def to_order_page(self):
        self.click(self.find(self._shop_page))


class AddOrder(OrderPage):
    _add_button = (By.XPATH,'//*[@class="el-main el-main-container"]/div/div/div/div/div/button')
    _ordertype_select = (By.XPATH,'//*[@class="el-dialog"]/div[2]/form/div/div/div/div/input')
    _ordertype_option = (By.XPATH,'//body/div[3]/div/div/ul/li')
    _shop_input = (By.XPATH,'//*[@class="el-dialog"]/div[2]/form/div[2]/div/div/div/input')
    _shop_option = (By.XPATH,'//body/div[4]/div/div/ul/li')
    _submit_button = (By.XPATH,'//*[@class="el-dialog__footer"]/div/button[2]')

    def to_add_form(self):
        self.click(self.find(self._add_button))

    def choose_order_type(self):
        self.click(self.find(self._ordertype_select))
        self.click(self.find(self._ordertype_option))

    def choose_shop(self,shopname):
        self.click(self.find(self._shop_input))
        self.write(self.find(self._shop_input),shopname)
        self.click(self.find(self._shop_option))

    def add_submit(self):
        self.click(self.find(self._submit_button))

    def add_order(self,shopname):
        self.to_add_form()
        self.choose_order_type()
        self.choose_shop(shopname)
        self.add_submit()


if __name__ == "__main__":
    a = AddOrder("http://vrs.uat1.rs.com/s/#/login")
    a.login("18721700000","123456")
    a.to_order_page()
    a.add_order("新增店铺")
