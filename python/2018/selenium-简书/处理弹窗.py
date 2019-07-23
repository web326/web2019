from  selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
url = 'http://www.baidu.com'
driver.get(url)
driver.implicitly_wait(2)
#鼠标悬停
link = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(link).perform()
time.sleep(1)
driver.find_element_by_class_name('setpref').click()
time.sleep(2)
driver.find_element_by_class_name('prefpanelgo').click()
time.sleep(2)
#接收弹窗
driver.switch_to.alert.accept()
driver.quit()
print('执行完成')
