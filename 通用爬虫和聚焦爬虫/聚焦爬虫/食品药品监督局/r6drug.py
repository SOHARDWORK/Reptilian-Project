import requests
import json
if __name__=="__main__":
    post_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    ids_list=[]
    all_data_list = []
    #首页ajax动态加载药品公司信息，获取公司id
    for i in range(1,6):
        page = str(i)
        data = {
            'on': 'true',
            'page': '1',
            'pageSize': '15',
            'productName':'',
            'conditionType': '1',
            'applyname':'',
            'applysn':'',
        }
        dic_list=requests.post(url=post_url,data=data,headers=headers).json()

        for comp in dic_list['list']:
            ids_list.append(comp['ID'])
    detail_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
    #拿到公司id，详情页也是通过ajax动态加载的，传递id值动态拿到详情信息
    for id in ids_list:
        detail_data = {
            'id':id
        }
        detail_json = requests.post(url=detail_url,data=detail_data,headers=headers).json()
        all_data_list.append(detail_json)
    with open('.//alldata.json','w',encoding='utf-8') as f:
        json.dump(all_data_list,fp=f,ensure_ascii=False)

