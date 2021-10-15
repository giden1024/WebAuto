#!usr/bin/env python
#-*- coding:utf -*-
'''
@author = 'mayuyang'
@file:learn_loop_2.py
@time:2019/3/224:44 PM
@desc:
'''
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.support.wait import WebDriverWait
from initlization import BrowserDriver
import time


class BasePage:

    def __init__(self,url,type="PC"):
        self.driver = BrowserDriver.BuildUpDriver().driver
        if type == "H5":
            self.driver = BrowserDriver.BuildUpDriver().build_up_h5_driver(url)
            time.sleep(3)
        else:
            self.driver = BrowserDriver.BuildUpDriver().build_up_driver(url)
            time.sleep(3)



    def find(self,locate) :
        ele = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locate))
        return ele

    def my_wait(self,second,locate,result):
        try:
            WebDriverWait(self.driver,second).until(lambda x:x.find_element(*locate).text == result)
        except TimeoutException as e:
            print("请求超时")

    def findall(self,locate):
        return self.driver.find_elements(*locate)

    def get_url(self,url):
        self.driver.get(url)

    def touch_ele(self,ele):
        TouchActions(self.driver).tap(ele).perform()

    def write(self,ele,content):
        # ele.js_click()
        # if ele.is_enabled():
        ele.click()
        ele.clear()
        ele.send_keys(content)

    def click(self,ele): # 使用js方法进行点击，如果元素无法使用，使用selenium元素的click()方法
        try:
            # 原始点击方法
            ele.click()
        except ElementClickInterceptedException:
            self.touch_ele(ele)
        except TimeoutException:
            # js点击，如果无效是不会报错的
            self.driver.execute_script("arguments[0].click();", ele)

    def click_out(self):
        ActionChains(self.driver).move_by_offset(800,400).click().perform()

    def get_text(self,ele):
        try:
            ele_text = ele.text
        except TimeoutException as t:
            ele_text = self.driver.execute_script("arguments[0].innerText;",ele)
        return ele_text

    def set_value(self,ele,value):
        print('arguments[0].setAttribute("value",%r);'%value,ele)
        self.driver.execute_script('arguments[0].setAttribute("value",%r);'%value,ele)

    def goto_url(self,url):
        self.driver.get(url)

    def scroll_move(self,direction="down"):

        js = "document.documentElement.scrollTop=10000"
        # 拖动到滚动条底部---向下
        if direction == "right":
            js = "document.documentElement.scrollLeft=10000"

        elif direction == "left":
            js = "var q=document.documentElement.scrollLeft=0"

        elif direction == "up":
            js = "var q=document.documentElement.scrollTop=0"

        # 执行命令
        self.driver.execute_script(js)


    def quit_driver(self):
        self.driver.quit()

    def accept_window(self):
        self.driver.switch_to.alert.accept()





if __name__ == "__main__":
    bs = BasePage("https://www.bing.com")


