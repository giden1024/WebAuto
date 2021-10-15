#!/usr/bin/env python
# encoding: utf-8
"""
@author: mayuyang
@time: 2020/8/4 14:10
@desc:
"""

import pytest
from pages.Sale.client_page import ClientPage


@pytest.mark.parametrize("username,password,url,login_text",
                         [("18721702701", "123456", "http://vrs.uat1.rs.com/s/#/login", "海狸逛逛销售系统")])
def test_login(username, password, url):

    client_page = ClientPage(url)
    client_page.login(username, password)
    text = login_page.get_header_text()

