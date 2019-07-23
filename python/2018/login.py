#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
    Created on 2018-10-17 16:43
    @author: 吴卫彬
'''
from selenium import webdriver
import os


#引入chromedriver.exe
#chromedriver = "C:/Users/wdjlw/AppData/Local/Chromium/Application/chromedriver234.exe"
#chromedriver = (r"C:\Users\wdjlw\AppData\Local\Chromium\Application\chromedriver239.exe")
chromedriver = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver  #改变环境变量
browser = webdriver.Chrome(chromedriver)

#设置浏览器需要打开的url
url = "https://10.85.7.76/icmp-web/#/login"
browser.get(url)

#在百度搜索框中输入关键字"python"
browser.find_element_by_class_name("kw").send_keys("python")
#单击搜索按钮
browser.find_element_by_id("su").click()

#关闭浏览器
#browser.quit()
