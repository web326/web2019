#调用javascript拖动滚动条
from  selenium import webdriver
import time
driver = webdriver.Firefox()
url= 'http://www.baidu.com'
driver.get(url)
#搜索
time.sleep(2)
driver.find_element_by_id('kw').send_keys('senlenium')
time.sleep(3)
driver.find_element_by_id('su').click()
#滚动条拖到底部
js ="document.documentElement.scrollTop=10000"
time.sleep(3)
driver.execute_script(js)
time.sleep(3)
#滚动条拖动到顶部
js= "document.documentElement.scrollTop=0"
driver.execute_script(js)

#左右拖动
#window_scro||to(左边距,上边距)
# js = "window_scro||to(200,1000)"
# driver.execute_script(js)
time.sleep(3)
driver.quit()
