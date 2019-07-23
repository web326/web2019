#coding=utf-8
from selenium import webdriver
#引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image,ImageEnhance
import pytesseract
import time


#登录,为了代码整洁，此处假设没有验证码
def login ():
    driver.find_element_by_class_name("el-input__inner").clear()
    driver.find_element_by_class_name("el-input__inner").send_keys("admin")  # username
    driver.find_element_by_xpath("//input[@type='password']").clear()
    driver.find_element_by_xpath("//input[@type='password']").send_keys("123456")  # password
    driver.find_element_by_class_name("el-button login-button el-button--primary").click()

#退出
def logout ():
    above = driver.find_element_by_class_name("el-icon-mgmt el-icon-mgmt-user")
    # 对定位到的元素（个人头像）进行悬停
    ActionChains(driver).move_to_element(above).perform()

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://192.168.11.5:3004/#/login")

#调用登录模块
login()

time.sleep(10)
#乱七八糟的其他操作。。。。。。

#退出
logout()
