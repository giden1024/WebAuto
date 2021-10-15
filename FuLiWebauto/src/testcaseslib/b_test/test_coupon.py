#!/usr/bin/env python
# encoding: utf-8
"""
@author: mayuyang
@time: 2020/8/28 14:47
@desc:
"""

from pages.B.coupon import AddCoupon
from common.common_file import get_url
import pytest
import os

class TestCoupon:
    uat_loing_url = get_url()['uat_b_login_url']
    a = AddCoupon(uat_loing_url)
    username = "18721705015"
    pwd = "123456"

    def coupon_add_all_process(self,coupon_name, coupon_type, discount_type, discount_number, threshold_number,
                   coupon_number, rule_text,goods_name=None):
        self.a.login(self.username,self.pwd)
        self.a.to_coupon()
        self.a.add_coupon(coupon_name, coupon_type, discount_type, discount_number, threshold_number,
                   coupon_number, rule_text,goods_name=None)
        self.a.quit_login()

    @pytest.mark.parametrize("coupon_name, coupon_type, discount_type, discount_number, "
                             "threshold_number,coupon_number, rule_text,goods_name",
                             [('M_店铺满减券', '店铺券', '满减券', '10000', '1000', '9', 'M_店铺满减使用规则', ''),
                              ('M_店铺满折券', '店铺券', '满折券', '0.1', '10000', '8', 'M_店铺满折券', ''),
                              ('M_店铺自定义券', '店铺券', '自定义', '店铺优惠信息', '店铺门槛信息', '7', 'M_店铺自定义券', ''),
                              ('M_商品满减券', '商品券', '满减券', '20000', '2000', '6', 'M_商品满减券', '测试商品1'),
                              ('M_商品满减券', '商品券', '满折券', '0.2', '20000', '5', 'M_商品满减券', '测试商品2'),
                              ('M_商品满减券', '商品券', '自定义', '商品优惠信息', '商品门槛信息','4','M_商品满减券','测试商品3')]
                               )
    def test_coupon_success(self,coupon_name, coupon_type, discount_type, discount_number, threshold_number,
                   coupon_number, rule_text,goods_name):
        self.coupon_add_all_process(coupon_name, coupon_type, discount_type, discount_number, threshold_number,
                   coupon_number, rule_text,goods_name)

        print(self.a.get_coupon_line1_info())


