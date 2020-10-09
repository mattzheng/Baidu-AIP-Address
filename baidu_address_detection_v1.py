
from aip import AipNlp
import json
import requests
import urllib
from urllib import parse
from requests import post
import json
import base64


class address_detection:
    def __init__(self):
        
        """ 5000次/天免费  QPS = 2 """
        self.APP_ID = 'xxxxxx'
        self.API_KEY = 'xxxxxx'  # 通用NLP的api_key
        self.SECRET_KEY = 'xxxxxx'  # 通用NLP的secret_key

    def get_access_token(self):
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(self.API_KEY,self.SECRET_KEY)
        response = requests.get(host)
        if response:
            #print(response.json())
            access_token = response.json()['access_token']
            return access_token
        else:
            print('error')

    def address(self,text):
        access_token = self.get_access_token()
        post_url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/address?charset=UTF-8&access_token={}'.format(access_token)
        #https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer?charset=UTF-8&access_token=24.f9ba9c5241b67688bb4adbed8bc91dec.2592000.1485570332.282335-8574074
        
        headers = {'Content-Type': 'application/json'}
        data = {"text":text}
        r = post(post_url, json.dumps(data), headers=headers)
        r.encoding = 'utf-8'
        return r.json()


if __name__ == '__main__':
    ad = address_detection()
    text = "上海市浦东新区纳贤路701号百度上海研发中心 F4A000 张三"
    text = '北京市朝阳区富康路姚家园3号楼5单元3305室马云15000000000邮编038300'
    ad.address(text)
    '''
        {'log_id': 1309384850054053888,
         'town': '张江镇',
         'city': '上海市',
         'county_code': '310115',
         'county': '浦东新区',
         'city_code': '310100',
         'phonenum': '',
         'province_code': '310000',
         'town_code': '310115125',
         'province': '上海市',
         'person': '张三',
         'detail': '纳贤路701号百度上海研发中心F4A000',
         'text': '上海市浦东新区纳贤路701号百度上海研发中心 F4A000 张三'}
    '''

