#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2021/10/28 17:22 
# @Author : mayuyang
# @File : config_parse.py 
# @desc:

import yaml
import os

config_path =os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + "/cfg/"
env_file = "env.yaml"
print(config_path+"new.txt")


def get_yaml():
    #  打开yaml文件
    with open(config_path+env_file ,"r" ,encoding="utf-8") as f:
        file_data = f.read()
        # yaml文件转为json
        yaml_data = yaml.load(file_data, Loader=yaml.FullLoader)
        return yaml_data


# 返回环境相关地址
def get_env_domain(env="test05",host="h5"):
    return get_yaml()['env'][env][host]


# 返回数据库相关
def get_database(env="test05"):
    return get_yaml()['database']['config'][env]


# 返回账号相关
def get_account(apply="df",env="test05"):
    # 返回一个json
    return get_yaml()['account'][apply][env]


if __name__ == "__main__":
    print(get_account())


