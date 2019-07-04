from selenium import webdriver
from time import sleep

bro = webdriver.Chrome(executable_path='./chromedriver.exe')
url = 'https://www.taobao.com'
bro.get(url)

#标签定位
search_input = bro.find_element_by_id('q')
#标签交互
search_input.send_keys('Iphon')
#执行js
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)
#定位搜索按钮并点击
btn = bro.find_element_by_css_selector('.btn-search')
btn.click()
bro.get('http://www.baidu.com')
bro.back()
sleep(2)
bro.forward()
sleep(5)
bro.quit()