from selenium import webdriver
from time import sleep
#模拟登录qq空间

bro = webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get('https://qzone.qq.com')
#查看账号密码登陆超链是不是在iframe中，是的话switch，在定位标签
bro.switch_to.frame('login_frame')
#定位账号密码登录
a_tag = bro.find_element_by_id('switcher_plogin')
a_tag.click()
username_tag = bro.find_element_by_id('u')
userpassword_tag = bro.find_element_by_id('p')
username_tag.send_keys('511221877')
userpassword_tag.send_keys('*********')
#定位登录按钮
btn_login = bro.find_element_by_id('login_button')
btn_login.click()
sleep(5)
bro.quit()