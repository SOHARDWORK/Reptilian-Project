# -*- coding:utf-8 -*-
import requests
if __name__ == '__main__':
    url = 'https://pic.qiushibaike.com/system/pictures/12116/121160861/medium/OXDFFXP22QBPN82M.jpg'
    #字符串：text，二进制：content，对象：json
    res = requests.get(url=url).content
    with open('.//qiubai.jpg','wb') as fp:
        fp.write(res)