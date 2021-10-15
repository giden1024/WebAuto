#!/usr/bin/env python
# encoding: utf-8
"""
@author: mayuyang
@time: 2020/8/28 14:50
@desc:
"""
import pymysql.cursors


class ExecuteFindKey:

    def __init__(self,env="test05",database="dffl_goods"):
        self.env = env
        self.database = database

    def get_sql_content(self,sql_content):
        # connection = None
        if self.env == "test05":
            connection = pymysql.connect(host='10.8.109.10',
                                     port=3306,
                                     user='psf',
                                     password='BOOT1234test',
                                     database=self.database,
                                     cursorclass=pymysql.cursors.DictCursor,
                                     autocommit=True) # 如果写了这一行，搜索返回的内容是键值对，否则是tuple
        elif self.env == "stage":
            connection = pymysql.connect(host='rm-uf68b0a9n8a8cb9fm.mysql.rds.aliyuncs.com',
                                         port=3306,
                                         user='allselect',
                                         password='allselect!qaz',
                                         database=self.database,
                                         cursorclass=pymysql.cursors.DictCursor)

        # cursor = connection.cursor()
        with connection:
            with connection.cursor() as cursor:
            # Create a new record
        # sql = "SELECT mme.key FROM mall_merchant_exchange mme WHERE merchant_id = %s"%merchant_id
                cursor.execute(sql_content)
                result = cursor.fetchall()
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        #         print(result)
            connection.commit()

        return result

    def get_key_from_merchant_sql(self,merchant_id):
        sql_content = "SELECT mme.key FROM mall_merchant_exchange mme WHERE merchant_id = %s"%merchant_id
        key = self.get_sql_content(sql_content)[0]['key']
        return key


    def get_code_and_orderNo_sql(self,merchant_id,limit):
        # sql_content = "SELECT sn,codes,amount FROM dffl_goods.t_code_goods_order WHERE `merchant_id` = %s AND `status` = '5' ORDER BY created_at DESC LIMIT %s;"%(merchant_id,limit)
        sql_content = r"SELECT sn,codes,amount FROM dffl_goods.t_code_goods_order WHERE merchant_id = '2014' AND `status` = '5' ORDER BY created_at DESC LIMIT 20;"
        print(sql_content)
        result = self.get_sql_content(sql_content)
        return result

if __name__ == "__main__":
    e = ExecuteFindKey(env="stage")
    print(e.get_code_and_orderNo_sql("2014","10"))
    # print(e.get_key_from_merchant_sql("2014"))