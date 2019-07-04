import requests
import json
if __name__=="__main__":
    post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    keyword = input('input keyword:')
    data = {
        'cname':'',
        'pid':'',
        'keyword': keyword,
        'pageIndex': '1',
        'pageSize': '10'
    }
    res = requests.post(url=post_url,data=data,headers=headers)
    page_text = json.loads(res.text)
    print(page_text)
    with open('.//beijing.json','w',encoding='utf-8') as fp:
        json.dump(page_text,fp=fp,ensure_ascii=False)
    print('over')
