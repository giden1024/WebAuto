#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2021/10/15 16:28 
# @Author : mayuyang
# @File : export_file.py 
# @desc:

# 目前功能比较单一，只是固定格式的json文件转为text。


def dict_to_text(filepath,filename,dict_con):
    with open(filepath + r"\\" + filepath,mode="a+") as f:
        for d in dict_con:
            f.read(d['sn'] + "")

