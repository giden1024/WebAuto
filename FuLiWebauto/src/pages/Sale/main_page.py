#!/usr/bin/env python
# encoding: utf-8
"""
@author: mayuyang
@time: 2020/8/4 14:32
@desc:
"""
from selenium.webdriver.common.by import By
from pages.Sale.login_page import LoginPage


class MainPage(LoginPage):

    _client_number = (By.XPATH, '//*[@class="user-container__statistics"]/div/p')  # title 客户数量
    _shop_number = (By.XPATH,'//*[@class="user-container__statistics"]/div[2]/p')  # title 店铺数量
    _order_number = (By.XPATH,'//*[@class="user-container__statistics"]/div[3]/p')  # title 订单数量
    _contract_number = (By.XPATH,'//*[@class="user-container__statistics"]/div[4]/p')  # title 合同数量
    _name_text = (By.XPATH,'//*[@class="el-header"]/div[2]/span/button/span')  # 用户名展示
    _mobile_text = (By.XPATH,'//*[@class="user-container__info"]/div/p[2]')  # 用户手机号
    _sign_out_button = (By.XPATH,'//*[@class="user-container__info"]/div/button')

    def user_info(self):
        user_info = {}
        user_info['客户数量'] = self.get_text(self.find(self._client_number))
        user_info['店铺数量'] = self.get_text(self.find(self._shop_number))
        user_info['订单数量'] = self.get_text(self.find(self._order_number))
        user_info['合同数量'] = self.get_text(self.find(self._contract_number))
        user_info['合伙人姓名'] = self.get_text(self.find(self._name_text))
        user_info['合伙人手机号'] = self.get_text(self.find(self._mobile_text))
        return user_info

    def sign_out(self):
        self.click(self.find(self._sign_out_button))


if __name__ == "__main__":
    m = MainPage("http://vrs.uat1.rs.com/s/#/login")
    m.login("18721700027","123456")
    print(m.user_info())
    m.sign_out()