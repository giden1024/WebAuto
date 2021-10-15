#!/user/bin/env python3
#coding=utf-8
'''
@author: mayuyang
@file: shop_page.py
@time: 2020/5/22 14:24
@desc:

'''
from selenium.webdriver.common.by import By
from pages.Sale.login_page import LoginPage

class SaleShop(LoginPage): # 销售店铺页面

    _shop_page = (By.XPATH,'//*[@class="el-menu"]/a[2]/li')
    _add_button = (By.XPATH,'//*[@class="titleButton flex_space_around"]/button')
    _edit_button = (By.XPATH,'//*[@class="el-table__body-wrapper is-scrolling-none"]/table/tbody/tr[1]/td[9]/div/button[1]')
    _view_button = (By.XPATH,'//*[@class="el-table__body-wrapper is-scrolling-none"]/table/tbody/tr[1]/td[9]/div/button[2]')

    # 跳转到商铺页面
    def to_shop(self):
        self.click(self.find(self._shop_page))

    # 点击添加按钮
    def add_shop(self):
        self.click(self.find(self._add_button))

    # 点击编辑按钮
    def edit_shop(self):
        self.click(self.find(self._edit_button))

    # 点击查看按钮
    def view_shop(self):
        self.click(self.find(self._view_button))


class SearchShop(SaleShop): # 搜索店铺的功能区域
    _search_shop_name = (By.XPATH,'//*[@class="el-row"]/div[1]/div/div/div/input')
    _search_shop_area = (By.XPATH,'//*[@class="el-row"]/div[2]/div/div/div/div/input')
    _search_shop_status = (By.XPATH,'//*[@class="el-row"]/div[3]/div/div/div/div/input')
    _search_shop_client = (By.XPATH, '//*[@class="el-row"]/div[4]/div/div/div/div/input')
    _search_shop_start_time = (By.XPATH, '//*[@class="el-row"]/div[5]/div/div/div/input[1]')
    _search_shop_end_time = (By.XPATH, '//*[@class="el-row"]/div[5]/div/div/div/input[2]')
    _search_button = (By.XPATH,'//*[@class="el-row"]/div[8]/div/button[1]')
    _clear_button = (By.XPATH,'//*[@class="el-row"]/div[8]/div/button[2]')

    def click_clear_button(self):
        pass

    def click_search_button(self):
        self.click(self.find(self._search_button))

    def search_name(self,ShopName):
        self.write(self.find(self._search_shop_name),ShopName)
        self.click(self.find(self._search_button))

    def search_area(self):
        pro_beijing = (By.ID,"cascader-menu-6403-0-0")
        city_beijing = (By.ID,"cascader-menu-676-1-0")
        self.click(self.find(self._search_shop_area))
        self.click(self.find(pro_beijing))
        self.click(self.find(city_beijing))

    def search_status(self):
        status_text = (By.XPATH,'html/body/div[6]/div/div/ul/li[6]/span')
        self.click(self.find(self._search_shop_status))
        self.click(self.find(status_text))

    def search_client(self,serachtext):
        self.write(self.find(self._search_shop_client),serachtext)


# 新增店铺页面
class AddShop(SaleShop):
    _add_button = (By.XPATH, '//*[@class="el-button el-button--primary el-button--small"]') # 新增按钮
    _name_input = (By.XPATH, '//*[@class="el-dialog__body"]/form/div[1]/div/div/input') # 输入姓名
    # 选择城市
    _city_select = (By.XPATH, '//*[@class="el-dialog__body"]/form/div[2]/div/div/div/input')
    _city_option = (By.XPATH, '//*[@class="el-popup-parent--hidden"]/div[3]/div/div/div/ul/li/span')
    _area_option = (By.XPATH, '//*[@class="el-popup-parent--hidden"]/div[3]/div/div[2]/div/ul/li/span')
    # 选择店铺
    _mail_input = (By.XPATH, '//*[@class="el-dialog__body"]/form/div[3]/div/div/div/input')
    _mail_option = (By.XPATH,'//body/div[4]/div/div/ul/li')
    # 详细地址输入
    _address_input = (By.XPATH, '//*[@class="el-dialog__body"]/form/div[4]/div/div/input')
    # 选择
    _client_input = (By.XPATH, '//*[@class="el-dialog__body"]/form/div[5]/div/div/div/input')
    _client_option = (By.XPATH, "//body/div[5]/div/div/ul/li")
    _shopstatus_select = ()
    _shopstatus_option = ()
    _remark_input = (By.XPATH, '//*[@class="el-dialog__body"]/form/div[7]/div/div/textarea')
    _submit_button = (By.XPATH, '//*[@class="el-dialog__footer"]/div/button[2]')

    def add(self): # 点击添加按钮
        self.click(self.find(self._add_button))

    def write_name(self, name=None): # 填写商铺名称
        self.write(self.find(self._name_input), name)

    def choose_city(self): # 选择城市
        self.click(self.find(self._city_select))
        self.click(self.find(self._city_option))
        self.click(self.find(self._area_option))

    def choose_mail(self): # 填写商场名称
        self.click(self.find(self._mail_input))
        self.click(self.find(self._mail_option))

    def write_address(self, address=None): # 填写具体地址
        self.write(self.find(self._address_input), address)

    def choose_client(self, clientname=None): # 选择
        self.write(self.find(self._client_input), clientname)
        self.click(self.find(self._client_option))

    def choose_shop_status(self):
        self.click(self.find(self._shopstatus_select))
        self.click(self.find(self._shopstatus_option))

    def write_remark(self, remark=None):
        self.write(self.find(self._remark_input), remark)

    def submit_add(self):
        self.click(self.find(self._submit_button))

    def add_shop(self, name, address, clientname, remark):
        self.add()
        self.write_name(name)
        self.write_address(address)
        self.write_remark(remark)
        self.choose_city()
        self.choose_mail()
        # self.choose_shop_status()
        self.choose_client(clientname)
        self.submit_add()


class AddPic(SaleShop): # 添加资质图片
    pass


class AddInvoice(SaleShop): # 添加发票信息
    pass


class AddContact(SaleShop):
    pass


class Edit(SaleShop): # 编辑店铺页面
    pass


class ViewShop(SaleShop): # 查看店铺页面
    pass


class VoidShop(SaleShop): # 废弃店铺页面
    _void_button = (By.XPATH, '//*[@class="el-table__body-wrapper is-scrolling-none"]/table/tbody/tr[1]/td[9]/div/button[3]')


if __name__ == "__main__":
    a = AddShop("http://vrs.uat1.rs.com/s/#/login")
    a.login("18721700000","123456")
    a.to_shop()
    a.add_shop(name="新增店铺",address="北京详细店铺地址",clientname="用户姓名",remark="店铺")
