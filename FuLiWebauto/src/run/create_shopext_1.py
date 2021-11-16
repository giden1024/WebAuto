#!usr/bin/env python
#-*- coding:utf -*-
'''
@author = 'mayuyang'
@file:learn_test1.py
@time:2021/11/118:15 PM
@desc: 随心兑1.0全流程
'''
from pages.shopext.create_order import EnterAmount
import time
from common.config_parse import get_env_domain,get_account

login_path = "/user/login?city=145"
pay_path = "/newBirthday/payBill?id="


# 生成订单
def creaet_order(merchant_id,env="test05",type="H5", times="1", amount="1"):

    link = get_env_domain(env=env)  # 根据环境获取访问地址
    account = get_account(env=env)  # 根据环境获取账号
    # print(link+login_path)
    e = EnterAmount(link+login_path, type=type)

    e.login(account["username"],account["pwd"])
    time.sleep(5)
    e.buy_code_times(times,link+pay_path+merchant_id,amount,account['pay_pwd'])


if __name__ == "__main__":
    # e = EnterAmount("https://m-test05.dongfangfuli.com/user/login?city=145",type="H5")
    # e.login("18721705015","123456")
    # # time.sleep(5)
    # url = "https://m-test05.dongfangfuli.com/newBirthday/payBill?id=5405"
    # amount = "1"
    # pwd_key = "1991"
    #
    # e.buy_code_times("8",url,amount,pwd_key)

    creaet_order("5405")