#!usr/bin/env python
#-*- coding:utf -*-
'''
@author = 'mayuyang'
@file:learn_test1.py
@time:2020/3/109:55 AM
@desc:
文件主要为执行所有的代码入口
'''
from imp import reload
import sys,os
import logging

sys.path.append(os.path.dirname(sys.modules[__name__].__file__))
reload(sys)

logging.basicConfig(filename="../log/mylog.log",level=1)


class CaseSuiteHandler:
    def get_test_case(self):
        #获取testcase
        pass

