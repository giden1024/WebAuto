#!/usr/bin/env python
# encoding: utf-8
"""
@author: mayuyang
@time: 2020/8/31 10:02
@desc:
"""
import pytest

from testcaseslib.b_test.my_add import my_add

list=[(1,2,3,4,5,6,7,8,9,0),(11,2,3,4,5,6,7,8,9,0)]


def test_1():
    print(0)

    @pytest.mark.parametrize("a,b,c,d,e,f,g,h,i,j",list)
    def test_add(a,b,c,d,e,f,g,h,i,j):
        assert my_add(a,b,c,d,e,f,g,h,i,j) == 1