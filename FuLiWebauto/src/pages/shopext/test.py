# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time : 2021/10/12 11:00
# # @Author : mayuyang
# # @File : test.py
# # @desc:
#
# class A:
#     def __init__(self,a,v="version"):
#         self.a = a
#         self.v = v
#
#     def p(self):
#         print(self.a)
#         print(self.v)
#
#
# class B(A):
#     def __init__(self,a,v,b="new"):
#         super(B, self).__init__(a,v)
#         self.b = b
#
#     def p(self):
#         print(self.a)
#         print(self.v)
#         print(self.b)
#
#
# if __name__ == "__main__":
#     b = B("a",v="v111",b="new1")
#     b.p()
#
for x in "111":
    print(x)
amount = "1121"
for num in str(amount):
    _number_span = ( '//span[text()="%s"]' % num)
    print(_number_span)