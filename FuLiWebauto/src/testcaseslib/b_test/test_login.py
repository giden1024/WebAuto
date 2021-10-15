#!usr/bin/env python
#-*- coding:utf -*-
'''
@author = 'mayuyang'
@file:learn_loop_2.py
@time:2019/4/245:42 PM
@desc:
'''

import pytest
from pages import LoginPage


@pytest.mark.parametrize("username,password,url,login_text",
                         [("18721702701", "123456", "http://vrs.uat1.rs.com/s/#/login", "海狸逛逛销售系统")])
def test_login(username, password, url, login_text):

    login_page = LoginPage(url)
    login_page.login(username, password)
    text = login_page.get_header_text()
    assert text == login_text



