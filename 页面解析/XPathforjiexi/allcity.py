from lxml import etree
import requests
if __name__ == '__main__':
    url = 'https://www.aqistudy.cn/historydata/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    html_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(html_text)
    hot_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
    all_city_names = []
    for li in hot_li_list:
        hot_city_name = li.xpath('./a/text()')[0]
        all_city_names.append(hot_city_name)

    city_name_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    for li in city_name_list:
        city_name = li.xpath('./a/text()')[0]
        all_city_names.append(city_name)
