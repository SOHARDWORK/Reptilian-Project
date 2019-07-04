import requests
if __name__ =='__main__':
    #指定url
    url = 'https://www.sogou.com/'
    #发起请求
    res = requests.get(url=url)
    #获取数据
    page_text = res.text#字符串响应数据
    print(page_text)
    #数据持久化
    with open('.//sougou.html','w',encoding='utf-8') as f:
        f.write(page_text)
