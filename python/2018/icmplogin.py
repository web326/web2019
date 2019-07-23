#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
    Created on 2018-10-17 16:43
    @author: 吴卫彬
'''
from selenium import webdriver
import os
import ssh


#引入chromedriver.exe
#chromedriver = "C:/Users/wdjlw/AppData/Local/Chromium/Application/chromedriver234.exe"
#chromedriver = (r"C:\Users\wdjlw\AppData\Local\Chromium\Application\chromedriver239.exe")
chromedriver = ("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
os.environ["webdriver.chrome.driver"] = chromedriver  #改变环境变量
browser = webdriver.Chrome(chromedriver)

#设置浏览器需要打开的url
url = "https://10.85.7.76/icmp-web/#/login"
browser.get(url)

#获取当前窗口句柄
h=browser.current_window_handle
print(h)
#获取所有句柄
all_h=browser.window_handles
print(all_h)

#在百度搜索框中输入关键字"python"
browser.find_element_by_xpath("//*[@id=\"login\"]/div[1]/form/div[1]/div/div/div/input").send_keys("icmp_admin")
#browser.find_element_by_xpath(("//*[@id="login"]/div[1]/form/div[1]/div/div/div/input").send_keys("icmp_admin")
#单击搜索按钮
browser.find_element_by_xpath("//*[@id=\"login\"]/div[1]/form/div[2]/div/div/div/input").send_keys("123456");

browser.find_element_by_xpath("//*[@id=\"keybtn\"]").click()
#关闭浏览器
#browser.quit()
