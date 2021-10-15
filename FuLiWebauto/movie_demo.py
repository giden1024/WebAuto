#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2021/1/18 14:03 
# @Author : mayuyang
# @File : movie_demo.py
import time

from selenium import webdriver
import requests
import os
from lxml import etree
from elasticsearch import Elasticsearch
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


def set_driver(url):

    chrome_options = webdriver.ChromeOptions()
    mobileEmulation = {'deviceName': 'iPhone 7'}
    # 手机模式
    # chrome_options.add_experimental_option('mobileEmulation', mobileEmulation)
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    # driver.maximize_window()
    driver.get(url)
    # driver.execute_script('window.scrollBy(0,200)')
    return driver


def link_es(url,port):
    es = Elasticsearch([url],port=port)
    # 忽略400以及404的消息
    # es.indices.create(index='test-index', ignore=400)
    # es.indices.delete(index='test-index', ignore=[400, 404])
    # # 查询默认登录1秒钟
    # es.cluster.health(wait_for_status='yellow', request_timeout=1)
    if es.ping():
        print(es.info())
    else:
        print("集群未启动")



def movie_manage():
    driver = set_driver("http://10.8.110.68:18091/")


def movie_pc():
    driver = set_driver("https://www-test05.dongfangfuli.com/newmovie/")
    # driver.find_element(By.XPATH, '//*[text()="退出登录"]')
    try:
        driver.find_element(By.XPATH,'//*[text()="退出登录"]')
    except Exception as nosuch:
        print("用户需要登录")

        driver.find_element(By.XPATH, '//*[text()="登录"]').click()
        print(driver.title)
        if "用户登录" in driver.title:
            pc_login(driver,"18721705015","123456")
            print("登录成功！")
    time.sleep(10)


def pc_login(driver,username,pwd):
    driver.find_element(By.ID, "user_name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(pwd)
    driver.find_element(By.ID, "confirm").click()


def test():
    driver = set_driver("http://www.dongfangfuli.com/?city=145")
    # driver.execute_script('window.scrollTo(0,969)')
    bdy = driver.find_element(By.XPATH, '//body')
    # bdy.click()
    bdy.send_keys(Keys.PAGE_DOWN)
    # driver.find_element()
    # driver.find_element(By.XPATH, '//*[text()="02-28"]').click()
    # driver.find_elements(By.XPATH, '//*[text()="选座购票"]')[0].click()
    time.sleep(10)
    # canvas = driver.find_element(By.XPATH, '//canvas')
    # ActionChains(driver).move_to_element_with_offset(canvas,590,190).click().perform()


if __name__ == "__main__":
    test()