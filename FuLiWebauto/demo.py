#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2021/1/11 13:12 
# @Author : mayuyang
# @File : demo.py

from selenium import webdriver
import requests
import os
from lxml import etree

img_path = os.path.abspath(os.path.dirname(__file__))

def save_pic(name,pic):
    file_path = img_path+"/img/"
    with open(file_path+name,'wb') as f1:
        f1.write(pic)


def get_img():

    chrome_options = webdriver.ChromeOptions()
    mobileEmulation = {'deviceName': 'iPhone 7'}
    chrome_options.add_experimental_option('mobileEmulation', mobileEmulation)
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome(options=chrome_options)
    # driver.maximize_window()
    driver.get("http://www.dongfangfuli.com/?city=145")
    driver.execute_script('window.scrollBy(0,200)')

    # li_len = len(driver.find_elements_by_xpath('//div[@class="honor"]/div/div/ul/li'))
    # print(len)
    # for x in range(li_len):
    #     a = driver.find_element_by_xpath('//div[@class="honor"]/div/div/ul/li[%s]/a/img'%(x+1))
    #     img_url = a.get_attribute("src")
    #     r = requests.get(img_url)
    #     save_pic("img"+str(x)+".png",r.content)



def get_fuli_url():
    html_text = '''
         <li><a href="http://m.sunyuwei.qa.psf-dev.com/tmall/birthday?city=145" class="external"><img src="//static.sunyuwei.qa.psf-dev.com/h5/img/index_2020/fuli01.png?v=3" alt=""></a></li>
                    <li><a href="http://m.sunyuwei.qa.psf-dev.com/common/activity/home?city=145" class="external"><img src="//static.sunyuwei.qa.psf-dev.com/h5/img/index_2020/fuli02.png?v=3" alt=""></a></li>
                    <li><a href="http://m.sunyuwei.qa.psf-dev.com/movie/list?city=145" class="external"><img src="//static.sunyuwei.qa.psf-dev.com/h5/img/index_2020/fuli03.png?v=3" alt=""></a></li>
                    <li><a href="http://m.sunyuwei.qa.psf-dev.com/mall?city=145" class="external"><img src="//static.sunyuwei.qa.psf-dev.com/h5/img/index_2020/fuli04.png?v=3" alt=""></a></li>
                    <li><a href="/tmall/activity/index " class="external"><img src="//static.sunyuwei.qa.psf-dev.com/h5/img/index_2020/fuli05.png?v=3" alt=""></a></li>
                    <li><a href="https://m.dongfangfuli.com/wap/health/index?city=145" class="external"><img src="//static.sunyuwei.qa.psf-dev.com/h5/img/index_2020/fuli06.png?v=3" alt=""></a></li>
                    <li><a href="http://m.sunyuwei.qa.psf-dev.com/drama_h5/home?city=145" class="external"><img src="//static.sunyuwei.qa.psf-dev.com/h5/img/index_2020/fuli07.png?v=3" alt=""></a></li>
                    <li><a href="http://m.sunyuwei.qa.psf-dev.com/scenery/list?city=145" class="external"><img src="//static.sunyuwei.qa.psf-dev.com/h5/img/index_2020/fuli08.png?v=3" alt=""></a></li>
                    <li><a href="http://m.sunyuwei.qa.psf-dev.com/tmall/book?city=145" class="external"><img src="//static.sunyuwei.qa.psf-dev.com/h5/img/index_2020/fuli09.png?v=3" alt=""></a></li>
                    <li><a href="http://m.sunyuwei.qa.psf-dev.com/prdouct/detail?id=6&amp;city=145" class="external"><img src="//static.sunyuwei.qa.psf-dev.com/h5/img/index_2020/fuli10.png?v=3" alt=""></a></li>
                    <li><a href="http://m.sunyuwei.qa.psf-dev.com/prdouct/detail?id=7&amp;city=145" class="external"><img src="//static.sunyuwei.qa.psf-dev.com/h5/img/index_2020/fuli11.png?v=3" alt=""></a></li>
                    <li><a href="http://m.sunyuwei.qa.psf-dev.com/news/bfd?city=145" class="external"><img src="//static.sunyuwei.qa.psf-dev.com/h5/img/index_2020/fuli12.png?v=3" alt=""></a></li>
    
    '''
    html = etree.HTML(html_text)
    for x in html.xpath("//li/a/@href"):
        if "http" in x:
            print(x.split(".")[-1].strip("com"))
        else:
            print(x)

def get_pc_url():
    with open("test_html","r",encoding="utf-8") as f1:
        html_text = f1.read()
    html = etree.HTML(html_text)
    for x in html.xpath("//li/a/@href"):
        if "http" in x:
            print(x.split(".")[-1].strip("com"))
        else:
            print(x)

def test_name():
    name_list = ["ISO27001信息安全管理体系认证证书",
              "2020安永复旦中国最具潜力企业奖",
              "阳光诚信联盟成员单位",
              "2020最具创新力企业",
              "上海绿洲公益发展中心捐赠证书",
              "2020年度最佳企业员工福利供应商",
              "南京工会会员服务平台合作伙伴",
              "2019(行业)影响力品牌",
              "中国物流与采购联合会科技进步奖一等奖",
              "2018中国年度优选雇主",
              "ISO27001信息安全管理体系认证证书",
              "36氪WISE2019新商业开创者",
              "阳光诚信联盟成员单位",
              "2019-2020年度亚洲最佳员工福利外包机构",
              "上海绿洲公益发展中心捐赠证书",
              "第九届中国公益节2019年度责任品牌奖",
              "南京工会会员服务平台合作伙伴",
              "第九届中国公益节2019年度公益践行奖",
              "上海市政府采购最具竞争力十强供应商",
              "2019年度最佳雇主奖"]

    print(len(name_list))

def test_name_2():
    name_list =[
          "ISO27001信息安全管理体系认证证书",
          "2020安永复旦中国最具潜力企业奖",
          "阳光诚信联盟成员单位",
          "2020最具创新力企业",
          "上海绿洲公益发展中心捐赠证书",

          "2020年度最佳企业员工福利供应商",
          "南京工会会员服务平台合作伙伴",
          "2019(行业)影响力品牌",
          "中国物流与采购联合会科技进步奖一等奖",
          "2018中国年度优选雇主",

          "ISO27001信息安全管理体系认证证书",
          "36氪WISE2019新商业开创者",
          "阳光诚信联盟成员单位",
          "2019-2020年度亚洲最佳员工福利外包机构",
          "上海绿洲公益发展中心捐赠证书",

          "第九届中国公益节2019年度责任品牌奖",
          "南京工会会员服务平台合作伙伴",
          "第九届中国公益节2019年度公益践行奖",
          "上海市政府采购最具竞争力十强供应商",
          "2019年度最佳雇主奖",
        
          "2020中国薪酬与福利供应商价值大奖",
          "2020中国十大影响力人力资源品牌奖",
          "2021大中华区薪酬福利创新大奖",
          "上海市政府采购最具竞争力十强供应商",
          "奥纳奖-2020年度社会责任 诚信品牌"
        ]

    honorArr = [
        "ISO27001信息安全管理体系认证证书",
        "2020安永复旦中国最具潜力企业奖",
        "阳光诚信联盟成员单位",
        "2020最具创新力企业",
        "上海绿洲公益发展中心捐赠证书",

        "2020年度最佳企业员工福利供应商",
        "南京工会会员服务平台合作伙伴",
        "2019(行业)影响力品牌",
        "中国物流与采购联合会科技进步奖一等奖",
        "2018中国年度优选雇主",

        "ISO27001信息安全管理体系认证证书",
        "36氪WISE2019新商业开创者",
        "阳光诚信联盟成员单位",
        "2019-2020年度亚洲最佳员工福利外包机构",
        "上海绿洲公益发展中心捐赠证书",

        "第九届中国公益节2019年度责任品牌奖",
        "南京工会会员服务平台合作伙伴",
        "第九届中国公益节2019年度公益践行奖",
        "上海市政府采购最具竞争力十强供应商",
        "2019年度最佳雇主奖",

        "2020中国薪酬与福利供应商价值大奖",
        "2020中国十大影响力人力资源品牌奖",
        "中国物流与采购联合会科技进步奖一等奖",
        "2021大中华区薪酬福利创新大奖",
        "上海市政府采购最具竞争力十强供应商",
        "奥纳奖-2020年度社会责任 诚信品牌"
    ]

    print(len(name_list))


def test_split():
    u = "http://m.sunyuwei.qa.psf-dev.com/mall?city=145"
    print("http" in u)


if __name__ == "__main__":
    pass