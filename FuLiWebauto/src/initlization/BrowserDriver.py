#!usr/bin/env python
#-*- coding:utf -*-
'''
@author = 'mayuyang'
@file:learn_loop_2.py
@time:2019/4/244:10 PM
@desc:
'''
from selenium import webdriver
import os


class BuildUpDriver:
    # caps = webdriver.DesiredCapabilities.CHROME.copy()
    # caps['args'] = ['--start-maximized', '--disable-infobars']
    # 存储本地driver的地址
    driver_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + "/file/driver/chromedriver.exe"
    # 浏览器选项
    chrome_options = webdriver.ChromeOptions()
    # 去除网页打开的时候，自动化的标识
    # chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    # chrome_options.add_argument("--unlimited-storage")
    chrome_options.add_argument("no-sandbox")
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_experimental_option('w3c', False) # 谷歌浏览器自带w3c检查，需要屏蔽掉

    prefs = {"":""}

    # prefs["credentials_enable_service"] = False
    # prefs["profile.password_manager_enabled"] = False
    # chrome_options.add_experimental_option("prefs", prefs)  ##关掉密码弹窗

    # chrome_options.add_argument("–disable -gpu")  # 谷歌文档提到需要加上这个属性来规避bug
    # chrome_options.add_argument("lang = zh_CN.UTF-8")  # 设置默认编码为utf-8
    # chrome_options.add_experimental_option("useAutomationExtension", False)  # 取消chrome受自动控制提示




    # chrome_options.add_experimental_option("prefs", {'profile.default_content_setting_values':{'notifications' : 2}})
    # 定义一个driver
    # driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
    driver = webdriver.Chrome

    def build_up_driver(self,url):    # 新建浏览器
        self.driver = webdriver.Chrome(executable_path=self.driver_path, options=self.chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(url)
        return self.driver

    def quit_driver(self):  # 关闭浏览器
        self.driver.quit()

    def build_up_h5_driver(self, url):  # 新建浏览器
        mobile_emulation = {'deviceName': 'iPhone 6/7/8'}
        # mobile_emulation = {
        #     "deviceMetrics": {"width": 375, "height": 1000, "pixelRatio": 3.0},  # 定义设备高宽，像素比
        #     # "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) "  # 通过UA来模拟
        #     #              "AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
        #     "userAgent":'iphone X'
        # }

        self.chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        # self.chrome_options.add_argument('window-size=500,750')  # 无用
        self.driver = webdriver.Chrome(executable_path=self.driver_path,options=self.chrome_options)
        # self.driver.set_window_size("500","1000")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(url)
        return self.driver



if __name__ == "__main__":
    newdriver = BuildUpDriver().build_up_h5_driver("https://www.baidu.com")
    # newdriver.get("1")

