#coding=utf-8

from selenium import webdriver
from LoginPublic import Login
import time


driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(5)
driver.get("http://192.168.11.5:3004/#/login")
time.sleep(5)
#调用登录模块
Login.login(driver)
