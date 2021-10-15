#!/user/bin/env python3
#coding=utf-8
'''
@author: mayuyang
@file: client_page.py
@time: 2020/5/22 14:24
@desc:

'''
from selenium.webdriver.common.by import By
from pages.Sale.login_page import LoginPage


class ClientPage(LoginPage):
    _client_page = (By.XPATH, '//*[@class="el-menu"]/a[1]/li')  # 左侧导航栏
    _login_name_text = (By.XPATH, '//*[@class="el-header"]/div[2]/span')
    # _area_text = (By.XPATH,'//*[@class="user-container__info"]/div/p[3]')
    # 以下的都是列表中的TITLE
    client_name = (By.XPATH, '//div[@class="tableList"]/div/div[2]/table/thead/tr/th[1]/div')

    # 跳转到客户页面
    def to_client_page(self):
        self.click(self.find(self._client_page))

    # 返回客户列表第一条客户信息
    def get_client_list_one(self):
        client_info = []
        for x in range(1, 7):
            client_info.append(self.get_text(self.find((By.XPATH,'//div[@class="tableList"]/div/div[3]/table'
                                                                 '/tbody/tr/td[%s]/div' %x))))
        return client_info


class SearchClient(ClientPage):
    _client_name_input = (By.XPATH,'//*[@class="el-card__body"]/div/form/div/div[1]/div/div/div/input')  # 客户名称输入框
    _owner_input = (By.XPATH,'//*[@class="el-card__body"]/div/form/div/div[2]/div/div/div/div/input')  # 负责人输入框
    _owner_option = (By.XPATH,'//body/div[2]/div[1]/div[1]/ul/li/span')  # 负责人选择项
    _source_input = (By.XPATH,'//*[@class="el-card__body"]/div/form/div/div[3]/div/div/div/div/input')  # 来源选择输入框
    _source_option = (By.XPATH,'//body/div[3]/div/div/ul/li/span[text()="线下"]')  # 来源和类别选择项的第一个选择
    _category_input = (By.XPATH,'//*[@class="el-card__body"]/div/form/div/div[4]/div/div/div/div/input')  # 类别选项输入框
    _category_option = (By.XPATH, '//body/div[4]/div/div/ul/li/span[text()="经销商"]') # 类别选项
    _partner_input = (By.XPATH,'//*[@class="el-card__body"]/div/form/div/div[5]/div/div/div/div/input')  # 参与者
    _partner_option = (By.XPATH,'/html/body/div[5]/div[1]/div[1]/ul/li/span')  #
    _start_time_search = (By.XPATH,'//*[@class="el-range-input"][1]')  # 查询开始时间
    _end_time_search = (By.XPATH, '//*[@class="el-range-input"][2]')  # 查询结束时间
    _search_button = (By.XPATH,'//*[@class="el-card__body"]/div/form/div[2]/button[1]')  # 查询按钮
    _search_clear_button = (By.XPATH,'//*[@class="el-card__body"]/div/form/div[2]/button[2]')  # 清空按钮
    _start_time_option = (By.XPATH, '//*[@class="el-picker-panel__body"]/div[1]/table/tbody/tr[4]/td[2]/div/span')  # 开始时间
    _end_time_option = (By.XPATH, '//*[@class="el-picker-panel__body"]/div[1]/table/tbody/tr[4]/td[3]/div/span')  # 结束时间

    def search_name(self,client_name):
        self.write(self.find(self._client_name_input),client_name)

    def search_owner(self,owner_name):
        self.write(self.find(self._owner_input),owner_name)
        self.click(self.find(self._owner_option))

    def search_source(self):
        self.click(self.find(self._source_input))
        self.click(self.find(self._source_option))

    def search_category(self):
        self.click(self.find(self._category_input))
        self.click(self.find(self._category_option))

    def search_partner(self,partner_name):
        self.write(self.find(self._partner_input),partner_name)
        self.click(self.find(self._partner_option))

    def search_time(self,start_time,end_time):
        self.click(self.find(self._start_time_search))
        self.click(self.find(self._start_time_option))
        self.click(self.find(self._end_time_option))

    def submit_search(self):
        self.click(self.find(self._search_button))

    def submit_clear_search(self):
        self.click(self.find(self._search_clear_button))

    def search_time_act(self,start_time,end_time):

        self.search_time(start_time,end_time)
        self.submit_search()


class AddClient(ClientPage):
    _add_button = (By.XPATH,'//*[@class="customer"]/div[1]/div[1]/div/div/div/button')  # 新增客户按钮
    _name_input = (By.XPATH,'//*[@class="el-dialog__body"]/form/div/div/div/input')  # 客户姓名输入框
    _mobile_input = (By.XPATH,'//*[@class="el-dialog__body"]/form/div[2]/div/div/input')  # 手机号输入框
    _source_input = (By.XPATH,'//*[@class="el-dialog__body"]/form/div[3]/div/div/div/input')
    _source_option = (By.XPATH,'//body/div[3]/div/div/ul/li/span[text()="官网"]')  # 来源选项，选项内容为官网
    _category_input = (By.XPATH,'//*[@class="el-dialog__body"]/form/div[4]/div/div/div/input')
    _category_option = (By.XPATH,'//body/div[4]/div/div/ul/li/span[text()="经销商"]')
    _partner_input = (By.XPATH,'//*[@class="el-dialog__body"]/form/div[5]/div/div/div/input')  # 参与者输入框
    _partner_option = (By.XPATH,'//body/div[5]/div/div/ul/li[1]/span')  # 参与者选项，第一项
    _remark_input = (By.XPATH,'//*[@class="el-dialog__body"]/form/div[6]/div/div/textarea')
    _submit_button = (By.XPATH,'//*[@class="el-dialog__footer"]/div/button[2]')

    def add(self):
        self.click(self.find(self._add_button))

    def write_name(self,name=None):
        self.write(self.find(self._name_input),name)

    def write_mobile(self,mobile=None):
        self.write(self.find(self._mobile_input),mobile)

    def choose_source(self):
        self.click(self.find(self._source_input))
        self.click(self.find(self._source_option))

    def choose_category(self):
        self.click(self.find(self._category_input))
        self.click(self.find(self._category_option))

    def choose_partner(self,partner_name=None):
        self.write(self.find(self._partner_input),partner_name)
        self.driver.implicitly_wait(5)
        self.click(self.find(self._partner_option))

    def write_remark(self,remark=None):
        self.write(self.find(self._remark_input),remark)

    def submit_add(self):
        self.click(self.find(self._submit_button))

    def add_client(self,name,mobile,partner_name,remark):
        self.add()
        self.write_name(name)
        self.write_mobile(mobile)
        self.write_remark(remark)
        self.choose_source()
        self.choose_category()
        # self.choose_client_status()
        self.choose_partner(partner_name)
        self.submit_add()


class ClientInfoList(ClientPage):
    # 获取列表中的用户信息数据
    tr,td = 1,1
    str_trs = '//*[@class="tableList"]/div/div[3]/table/tbody/tr'
    str_td = '//*[@class="tableList"]/div/div[3]/table/tbody/tr[%s]/td'%tr
    str_tds = '//*[@class="tableList"]/div/div[3]/table/tbody/tr[%s]/td[%s]/div'%(tr,td)

    def info_list(self):
        info_list = []
        global tr, td
        for tr in range(1,len(self.findall((By.XPATH,self.str_trs)))+1):
            for td in range(1,len(self.findall((By.XPATH,self.str_td)))):
                text = self.get_text(self.find((By.XPATH, '//*[@class="tableList"]/div/div[3]/table/tbody/'
                                                          'tr[%s]/td[%s]/div' % (tr, td))))
                # text = self.get_text(self.find((By.XPATH,self.str_tds)))
                info_list.append(text)
        print(info_list)


class EditClient(AddClient):
    _edit_button = (By.XPATH, '//*[@class="tableList"]/div/div[3]/table/tbody/tr[1]/td[9]/div/button[1]')

    def edit(self, name, mobile, partner_name, remark):
        self.click(self.find(self._edit_button))
        self.add_client(name, mobile, partner_name, remark)


class ViewClient(ClientPage):
    _view_button = (By.XPATH,'//*[@class="tableList"]/div/div[3]/table/tbody/tr[1]/td[9]/div/button[2]')
    _name_text = (By.XPATH, '//*[@class="name-text"]')
    _source_info = (By.XPATH, '//*[@class="body-info"]/form/div/div[1]/div/div/div')
    _phone_info = (By.XPATH, '//*[@class="body-info"]/form/div/div[3]/div/div/div')
    _category_info = (By.XPATH, '//*[@class="body-info"]/form/div/div[4]/div/div/div')
    _principal_info = (By.XPATH, '//*[@class="body-info"]/form/div/div[6]/div/div/div')
    _partner_info = (By.XPATH, '//*[@class="body-info"]/form/div/div[7]/div/div/div')
    _remark_info = (By.XPATH, '//*[@class="body-info"]/form/div/div[8]/div/div/div')

    def view(self,client_name):
        self.click(self.find(self._view_button))
        return self.get_text(self.find(self._name_text)) == client_name

    def get_client_info(self): # 获取用户的基本数据，
        client_info = []
        for x in [1,3,4,6,7,8]:
            client_info.append(self.get_text(self.find((By.XPATH,'//*[@class="body-info"]/form/div/div[%s]/div/div/div' %x))))
        return client_info


if __name__ == "__main__":
    # v = ViewClient("http://vrs.uat1.rs.com/s/#/login")
    # v.login("18721702701", "123456")
    # if v.view("测试1"):
    #     print(v.get_client_info())
    # else:
    #     time.sleep(2)
    #     print(v.get_client_info())

    s = SearchClient("http://vrs.uat1.rs.com/s/#/login")
    s.login("18721702701", "123456")
    s.search_time_act('2020/08/10','2020/08/12')


