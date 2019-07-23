# coding=utf-8
from selenium import webdriver
# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image,ImageEnhance
import pytesseract
import time

# 定义一个 Login类
class Login(object):

    # Login 类有两个方法，一是登录，一是退出
    def login (driver):
        driver.find_element_by_class_name("el-input__inner").clear()
        driver.find_element_by_class_name("el-input__inner").send_keys("admin")  # username
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("123456")  # password
        # 这个类名是是复合类名，不能用来进行定位
        # driver.find_element_by_class_name("el-button login-button el-button--primary").click()
        driver.find_element_by_xpath("//button[@type = 'button']").click()


    # 退出
    def logout(driver):
        above = driver.find_element_by_class_name("el-icon-mgmt el-icon-mgmt-user")
        # 对定位到的元素（个人头像）进行悬停
        ActionChains(driver).move_to_element(above).perform()
        driver.find_element_by_class_name("el-dropdown-menu__item").click()
