from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
browser = webdriver.Chrome("./chromedriver", chrome_options=options)

browser.get("https://www.jianshu.com/")

for i in range(3):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# print(browser)
for j in range(10):
    try:
        button = browser.execute_script("var a = document.getElementsByClassName('load-more'); a[0].click();")
        time.sleep(2)
    except:
        pass
#
titles = browser.find_elements_by_class_name("title")
with open("article_jianshu.txt", "w", encoding="utf-8") as f:
    for t in titles:
        try:
            f.write(t.text + " " + t.get_attribute("href"))
            f.write("\n")
        except TypeError:
            pass
