#!usr/bin/env python
#-*- coding:utf -*-
'''
@author = 'mayuyang'
@file:learn_test1.py
@time:2021/11/96:28 PM
@desc:
'''
import hashlib


def sign(str):
    # 创建md5对象
    hl = hashlib.md5()
    # 更新hash对象的值，如果不使用update方法也可以直接md5构造函数内填写
    # md5_obj=hashlib.md5("123456".encode("utf-8")) 效果一样
    hl.update(str.encode("utf-8"))
    return hl.hexdigest().upper()  # 当前所有的加密内容都为大写



def get_sign_by_method(method_name,merchant,code,amount,se):
    pass


