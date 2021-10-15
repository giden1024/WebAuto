#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2021/10/15 16:28 
# @Author : mayuyang
# @File : export_file.py 
# @desc:

# 目前功能比较单一，只是固定格式的json文件转为text。
import os

# con = [{'sn': '516341889422146011917507', 'codes': '839475255712', 'amount': 100}, {'sn': '516341888892146011917257', 'codes': '323406879444', 'amount': 100}, {'sn': '516341106672146011917952', 'codes': '541081040483', 'amount': 100}, {'sn': '516341104652146011917952', 'codes': '172458257426', 'amount': 100}, {'sn': '516341104532146011917820', 'codes': '699761134625', 'amount': 100}, {'sn': '516340969772146011917551', 'codes': '727998315885', 'amount': 5}, {'sn': '516340967112146011917583', 'codes': '265882985023', 'amount': 100}, {'sn': '516340947022146011917273', 'codes': '851639213261', 'amount': 140}, {'sn': '516336574872141342049119', 'codes': '842999828533', 'amount': 470}, {'sn': '516329101602145402621882', 'codes': '448740016545', 'amount': 800}, {'sn': '516329101192145402621137', 'codes': '418475845185', 'amount': 800}, {'sn': '516329019062145402621740', 'codes': '488770456046', 'amount': 800}, {'sn': '516324604762143312211902', 'codes': '284583659886', 'amount': 470}, {'sn': '516309316852143312211848', 'codes': '799795581428', 'amount': 470}, {'sn': '516305734642146011917693', 'codes': '742464022571', 'amount': 100}, {'sn': '516299581512146011917934', 'codes': '202236445370', 'amount': 100}, {'sn': '516297112382146011917857', 'codes': '450559059823', 'amount': 100}, {'sn': '516297112282146011917898', 'codes': '621476219632', 'amount': 100}, {'sn': '516297111442146011917611', 'codes': '918399960069', 'amount': 100}, {'sn': '516297111342146011917875', 'codes': '105701856513', 'amount': 100}]
# file_path = os.path.dirname(__file__)
# print(file_path)
# filename = "my.txt"
# name = file_path + "/" + filename
# print(name)


def dict_to_text(filepath,filename,dict_con):
    with open(filepath + r"\\" + filename,mode="w+",encoding="utf-8") as f:
        f.writelines("东福订单号" + "\t\t" + "券码"+ "\t\t" + "金额（分）" + "\t\t" + "\n")
        for d in dict_con:
            # print(d)
            f.writelines(str(d['sn']) + "\t\t" + str(d['codes']) + "\t\t" + str(d["amount"]) + "\t\t" + "\n")


if __name__ == "__main__":
    # dict_to_text(file_path,filename,con)
    pass