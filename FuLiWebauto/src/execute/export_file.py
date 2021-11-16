#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2021/10/15 16:28 
# @Author : mayuyang
# @File : export_file.py 
# @desc:

# 目前功能比较单一，只是固定格式的json文件转为text。
import os
from ruamel import yaml
from execute.execute_sql import ExecuteFindKey

# con = [{'sn': '516341889422146011917507', 'codes': '839475255712', 'amount': 100}, {'sn': '516341888892146011917257', 'codes': '323406879444', 'amount': 100}, {'sn': '516341106672146011917952', 'codes': '541081040483', 'amount': 100}, {'sn': '516341104652146011917952', 'codes': '172458257426', 'amount': 100}, {'sn': '516341104532146011917820', 'codes': '699761134625', 'amount': 100}, {'sn': '516340969772146011917551', 'codes': '727998315885', 'amount': 5}, {'sn': '516340967112146011917583', 'codes': '265882985023', 'amount': 100}, {'sn': '516340947022146011917273', 'codes': '851639213261', 'amount': 140}, {'sn': '516336574872141342049119', 'codes': '842999828533', 'amount': 470}, {'sn': '516329101602145402621882', 'codes': '448740016545', 'amount': 800}, {'sn': '516329101192145402621137', 'codes': '418475845185', 'amount': 800}, {'sn': '516329019062145402621740', 'codes': '488770456046', 'amount': 800}, {'sn': '516324604762143312211902', 'codes': '284583659886', 'amount': 470}, {'sn': '516309316852143312211848', 'codes': '799795581428', 'amount': 470}, {'sn': '516305734642146011917693', 'codes': '742464022571', 'amount': 100}, {'sn': '516299581512146011917934', 'codes': '202236445370', 'amount': 100}, {'sn': '516297112382146011917857', 'codes': '450559059823', 'amount': 100}, {'sn': '516297112282146011917898', 'codes': '621476219632', 'amount': 100}, {'sn': '516297111442146011917611', 'codes': '918399960069', 'amount': 100}, {'sn': '516297111342146011917875', 'codes': '105701856513', 'amount': 100}]
# file_path = os.path.dirname(__file__)
# print(file_path)
# filename = "my.txt"
# name = file_path + "/" + filename
# print(name)

secret_yaml = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + "/cfg/" + "secret.yaml"


def dict_to_text(filepath,filename,dict_con):
    with open(filepath + r"\\" + filename,mode="w+",encoding="utf-8") as f:
        f.writelines("东福订单号" + "\t\t" + "券码"+ "\t\t" + "金额（分）" + "\t\t" + "\n")
        for d in dict_con:
            # print(d)
            f.writelines(str(d['sn']) + "\t\t" + str(d['codes']) + "\t\t" + str(d["amount"]) + "\t\t" + "\n")


def execute_secret(env):  # 把sql搜索出来的内容更新为merchantID：secret的粗暴格式，返回的内容是dict
    secret_list = ExecuteFindKey(env).get_key_from_merchant_sql()
    new_dict = {}
    for m_dict in secret_list:
        new_dict.update({m_dict['merchant_id']:m_dict['key']})
    return new_dict


def list_to_yaml(env,yaml_file):

    secret_dict = execute_secret(env)
    # 先读取文件，根据环境拉取不同环境的数据
    with open(yaml_file,mode="r",encoding="utf-8") as f:
        data = f.read()
    yaml_data = yaml.safe_load(data)
    # print(yaml_data)
    yaml_data[env] = secret_dict
    with open(secret_yaml, mode="w+", encoding="utf-8") as f:
        # 存储的时候，default_flow_style表示会按照yaml格式去存储
        yaml.dump(data=yaml_data, stream=f, allow_unicode=True,default_flow_style=False)




if __name__ == "__main__":
    # dict_to_text(file_path,filename,con)
    list_to_yaml("pro",yaml_file=secret_yaml)
