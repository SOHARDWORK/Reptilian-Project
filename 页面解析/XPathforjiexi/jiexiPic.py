from lxml import etree
import requests
import os
if __name__ == '__main__':
    url = 'http://pic.netbian.com/4kmeinv/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    res = requests.get(url=url,headers=headers)
    res.encoding = res.apparent_encoding
    html_text = res.text
    tree = etree.HTML(html_text)
    li_lsit = tree.xpath('//div[@class="slist"]//li')
    if not os.path.exists('./meinv'):
        os.mkdir('./meinv')
    for li in li_lsit:
        img_src = 'http://pic.netbian.com'+li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
        img_data = requests.get(url=img_src,headers=headers).content
        save_path = './meinv/'+img_name
        with open(save_path,'wb') as fp:
            fp.write(img_data)
