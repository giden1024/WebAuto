#!/usr/bin/env python
# encoding: utf-8
"""
@author: mayuyang
@time: 2020/8/11 17:16
@desc:
"""
from selenium import webdriver
import os

def get_config_path():
    current_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    config_path = current_path + r"\cfg\config.cfg"
    return config_path

def get_url():
    url_dict = {}
    config_path = get_config_path()
    with open(config_path) as f1:
        for x in f1.read().split("\n"):
            url_list = x.split("=")
            url_dict[url_list[0]] = url_list[1]
            # url_dict[x[0]] = x[1]

    UAT_S_LOGIN = url_dict['sale_uat_url'] + url_dict['login_path']
    UAT_S_INDEX = url_dict['sale_uat_url'] + url_dict['index_path']
    UAT_B_LOGIN = url_dict['b_uat_url']

    return {"uat_s_login_url":UAT_S_LOGIN,
            "uat_s_index_url":UAT_S_INDEX,
            "uat_b_login_url":UAT_B_LOGIN}


if __name__ == "__main__":
    print(get_url()['uat_b_login_url'])
