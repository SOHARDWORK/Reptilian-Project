import requests
import json
if __name__ == '__main__':
    #指定url
    post_url = 'https://fanyi.baidu.com/sug'
    #ua伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    wd = input('input word:')
    #参数组装
    data = {
        'kw': wd
    }
    # 发送post请求
    res = requests.post(url=post_url, data=data, headers=headers)
    dic_obj = res.json()
    print(dic_obj)
    # 持久存储
    filename = wd+'.json'
    with open(filename,'w',encoding='utf-8') as fp:
        json.dump(dic_obj,fp=fp,ensure_ascii=False)
    print('over')