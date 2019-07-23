#coding=utf-8
from selenium import webdriver
#引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image,ImageEnhance
import pytesseract
import time
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://192.168.11.5:3004/#/login")

#登录
driver.find_element_by_class_name("el-input__inner").send_keys("admin")#username
driver.find_element_by_xpath("//input[@type='password']").send_keys("123456")#password

#浏览器页面截屏
driver.get_screenshot_as_file('/Users/guxuecheng/Desktop/screenImg.png')

#定位验证码位置及大小
location = driver.find_element_by_class_name('captcha').location
size = driver.find_element_by_class_name('captcha').size
left = location['x']
top =  location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']

#从文件读取截图，截取验证码位置再次保存
img = Image.open('/Users/guxuecheng/Desktop/screenImg.png').crop((left,top,right,bottom))
img = img.convert('L')          #转换模式：L | RGB
img = ImageEnhance.Contrast(img)#增强对比度
img = img.enhance(2.0)          #增加饱和度
img.save('/Users/guxuecheng/Desktop/screenImg.png')

#读取识别验证码
yanzhengma = Image.open('/Users/guxuecheng/Desktop/screenImg.png')
text = pytesseract.image_to_string(yanzhengma).strip()
driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/form/div[3]/div/div/div[1]/div/input').send_keys(text)

#登录按钮
driver.find_element_by_class_name("el-button login-button el-button--primary")

time.sleep(5)

#退出
above = driver.find_element_by_class_name("el-icon-mgmt el-icon-mgmt-user")
#对定位到的元素（个人头像）进行悬停
ActionChains(driver).move_to_element(above).perform()
#定位到退出按钮并点击
exit = driver.find_element_by_class_name("el-dropdown-menu__item").click()
