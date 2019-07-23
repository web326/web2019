from  selenium import webdriver
import time
import logging
#开启debug获取服务端与客户端的交互信息
logging.basicConfig(level=logging.DEBUG)
driver = webdriver.Firefox()
url= 'http://zhtb.hcstec.com/login/login.html'
driver.get(url)
driver.find_element_by_xpath('/html/body/div/div/form/div[1]/select').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div/div/form/div[1]/select/option[2]').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/form/div[2]/input').send_keys('142630170611011230')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/form/div[3]/input').send_keys('123456')
time.sleep(2)
driver.find_element_by_xpath('/html/body/div/div/form/button').click()
