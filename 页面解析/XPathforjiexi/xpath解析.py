from lxml import etree
import requests
if __name__ == '__main__':
    url = 'https://bj.58.com/ershoufang/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    html_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(html_text)
    li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
    fp = open('./58.txt','w',encoding='utf-8')
    for li in li_list:
        title = li.xpath('./div[2]/h2/a/text()')[0]
        print(title)
        fp.write(title+'\n')
