from  selenium import webdriver
import time
driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(3)
url = 'http://www.baidu.com'
driver.get(url)
#获致当前页面的句柄
search_hand= driver.current_window_handle
print(search_hand)
driver.find_element_by_link_text('登录').click()
time.sleep(2)
driver.find_element_by_link_text('立即注册').click()

all_hands= driver.window_handles
#进入注册页面
for hand in all_hands:
    if hand != search_hand:
        driver.switch_to.window(hand)
        driver.find_element_by_id('TANGRAM__PSP_3__userName').send_keys('12333')
        time.sleep(1)
        driver.find_element_by_id('TANGRAM__PSP_3__phone').send_keys('1233390000')
for hand in all_hands:
    if hand == search_hand:
        driver.switch_to.window(hand)
        driver.find_element_by_id('kw').send_keys('python')
        driver.find_element_by_class_name('bg_s_btn').click()
driver.quit()
