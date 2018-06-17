# -*- coding: utf-8 -*-
"""
处理 API 响应
状态码为 200 ，因此我们知道请求成功了。响应字典只包含三个键： 'items' 、 'total_count' 和 'incomplete_results' 。
"""
__author__ = 'YanLe'

import requests
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r= requests.get(url)

print('Status code: ', r.status_code)

# 将API相应存储到一个变量里面
response_dict=r.json()

# 处理结果
print(response_dict.keys())