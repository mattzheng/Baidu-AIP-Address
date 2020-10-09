# Baidu-AIP-Address
百度最近推出了地址识别，不过python SDK没有更新，只能用请求的方式

其中，自己需要在百度后台拿到。

```
APP_ID = 'xxxxxx'
API_KEY = 'xxxxxx'
SECRET_KEY = '
```

使用：

```
ad = address_detection()
text = "上海市浦东新区纳贤路701号百度上海研发中心 F4A000 张三"
text = '北京市朝阳区富康路姚家园3号楼5单元3305室马云15000000000邮编038300'
ad.address(text)
```

输出的结果：

```
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
```



关联的项目：

- 百度API官方的github:  https://github.com/Baidu-AIP/python-sdk
- 百度地址识别官方文档:https://ai.baidu.com/ai-doc/NLP/vk6z52h5n


