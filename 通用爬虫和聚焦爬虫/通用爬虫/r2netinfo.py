import requests
if __name__ == "__main__":
    url = 'https://www.sogou.com/web'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    # 处理url所携带的参数
    kw = input('input kw')
    param = {
        'query':kw
    }
    res = requests.get(url=url, params=param,headers=headers)
    page_text = res.text
    filename = kw+'.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(page_text)
    print(filename, "保存成功")
