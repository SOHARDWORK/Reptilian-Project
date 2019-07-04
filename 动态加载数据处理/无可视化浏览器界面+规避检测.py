from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
from time import sleep

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
option = Options()
option.add_experimental_option('excludeSwitches',['enable-automation'])

bro = webdriver.Chrome(executable_path='./chromedriver.exe',chrome_options=chrome_options,options=option)
#无可视化界面，无头浏览器
bro.get('http://www.baidu.com/')
print(bro.page_source)
bro.quit()
