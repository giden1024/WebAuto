#!/usr/bin/env python
# encoding: utf-8
"""
@author: mayuyang
@time: 2020/8/28 14:50
@desc: 本文件，将数据库中的数据取出，然后处理为list-dict文件。
"""
import pymysql.cursors
from common.config_parse import get_database

class ExecuteFindKey:

    def __init__(self,env="test05",database="dffl_goods"):
        self.env = env
        self.database = database

    def get_sql_content(self,sql_content):
        print(get_database())
        # self.env = None
        database_con = get_database(self.env)  # env指对应的环境，包括test05/stage/pro
        connection = pymysql.connect(host=database_con['host'],
                                 port=database_con['port'],
                                 user=database_con['user'],
                                 password=database_con['pwd'],
                                 database=self.database,
                                 cursorclass=pymysql.cursors.DictCursor,
                                 autocommit=True) # 如果写了这一行，搜索返回的内容是键值对，否则是tuple

        with connection:
            with connection.cursor() as cursor:
                cursor.execute(sql_content)
                result = cursor.fetchall()
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        #         print(result)
            connection.commit()

        return result

    def get_key_from_merchant_sql(self,merchant_id=None):
        if merchant_id:
            sql_content = "SELECT mme.key FROM mall_merchant_exchange mme WHERE merchant_id = %s"%merchant_id
            key_list = self.get_sql_content(sql_content)

        else:
            sql_content = "SELECT mme.merchant_id,mme.key FROM mall_merchant_exchange mme"
            key_list = self.get_sql_content(sql_content)

        return key_list



    def get_code_and_orderNo_sql(self,merchant_id,limit):
        # sql_content = "SELECT sn,codes,amount FROM dffl_goods.t_code_goods_order WHERE `merchant_id` = %s AND `status` = '5' ORDER BY created_at DESC LIMIT %s;"%(merchant_id,limit)
        sql_content = r"SELECT sn,codes,amount FROM dffl_goods.t_code_goods_order WHERE merchant_id = '2014' AND `status` = '5' ORDER BY created_at DESC LIMIT 20;"
        # print(sql_content)
        result = self.get_sql_content(sql_content)
        return result


if __name__ == "__main__":
    e = ExecuteFindKey(env="test05")
    # print(e.get_code_and_orderNo_sql("2014","10"))
    print(e.get_key_from_merchant_sql())