import requests
import json
if __name__=="__main__":
    url = 'https://movie.douban.com/j/chart/top_list'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    params = {
        'type':'24',
        'interval_id':'100:90',
        'action':'',
        'start':'0',
        'limit':'20'
    }
    res = requests.get(url=url,params=params,headers=headers)
    list_json = res.json()
    with open('.//xiju.json','w',encoding='utf-8') as fp:
        json.dump(list_json,fp=fp,ensure_ascii=False)
    print('over')