#添加cookies
import time
from  selenium import webdriver
driver  = webdriver.Firefox()
url= 'http://www.baidu.com'
driver.get(url)
driver.add_cookie({'name':'123','value':'333'})
cookies = driver.get_cookies()
for cookie in  cookies:
    print('%s ->%s' % (cookie['name'],cookie['value']))
print('cookies 操作完成')
time.sleep(2)
driver.quit()
