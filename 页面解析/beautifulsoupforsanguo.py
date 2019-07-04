import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    html_text = requests.get(url=url,headers=headers).text
    beautifulsoup = BeautifulSoup(html_text,'lxml')
    li_list = beautifulsoup.select('.book-mulu > ul > li')
    fp = open('./sanguo.txt','w',encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url ='http://www.shicimingju.com' + li.a['href']
        detail_text = requests.get(url=detail_url,headers=headers).text
        detail_soup = BeautifulSoup(detail_text,'lxml')
        div_tag = detail_soup.find('div',class_='chapter_content')
        content = div_tag.text
        fp.write(title+':'+content+'\n')