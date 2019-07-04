from selenium import webdriver
from lxml import etree
from time import sleep
#实例化一个浏览器对象（传入参数为浏览器驱动）
bro = webdriver.Chrome(executable_path='./chromedriver.exe')
#让浏览器发出请求
url = 'http://125.35.6.84:81/xk/'
bro.get(url)
#获取浏览器当前页面的页面源码数据
html_text = bro.page_source
#解析企业名称
tree = etree.HTML(html_text)
li_list = tree.xpath('//ul[@id="gzlist"]/li')
for li in li_list:
    name = li.xpath('./dl/@title')[0]
    print(name)

#不要过早关闭浏览器
sleep(5)
bro.quit()