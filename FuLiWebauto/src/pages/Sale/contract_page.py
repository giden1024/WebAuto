#!/usr/bin/env python
# encoding: utf-8
'''
@author: mayuyang
@time: 2020/6/19 9:45
@desc:
'''
from selenium.webdriver.common.by import By
from pages.Sale.login_page import LoginPage


class ContractPage(LoginPage):
    _contract_page = (By.XPATH, '//*[@class="el-menu"]/a[4]/li')  # 左侧导航栏
    # 以下的都是列表中的TITLE
    client_name = (By.XPATH, '//div[@class="tableList"]/div/div[2]/table/thead/tr/th[1]/div')
    # 合同编号
    _contract_number = (By.XPATH, '//div[@class="el-card__body"]/div/div[3]/table/tbody/tr[1]/td[1]/div/div/span[1]')

    # 跳转到客户页面
    def to_contract_page(self):
        self.click(self.find(self._contract_page))

    # 返回客户列表第一条客户信息
    def get_contract_list_one(self):

        contract_info = []
        contract_info.append(self.get_text(self.find(self._contract_number)))
        for x in range(2, 9):
            contract_info.append(self.get_text(self.find((By.XPATH, '//div[@class="el-card__body"]/div/div[3]/table'
                                                                    '/tbody/tr[1]/td[%s]/div' % x))))
        return contract_info


class SearchContract(ContractPage):
    _shop_name_input = (By.XPATH, '')
    _contract_type = (By.XPATH, '')



class ViewContract():
    _view_button = (By.XPATH, '')

class VoidContract():
    pass

class EditContract():
    pass

if __name__ == "__main__":
    c = ContractPage("http://vrs.uat1.rs.com/s/#/login")
    c.login("18721702701","123456")
    c.to_contract_page()
    print(c.get_contract_list_one())

