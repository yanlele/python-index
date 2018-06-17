# -*- coding: utf-8 -*-
"""
处理响应字典
状态码为 200 ，因此我们知道请求成功了。响应字典只包含三个键： 'items' 、 'total_count' 和 'incomplete_results' 。
"""
__author__ = 'YanLe'

import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

print('Status code: ', r.status_code)

# 将API相应存储到一个变量里面
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])      # 搜索到的信息总数

# 搜索相关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))        # 我们获得了多少个仓库的信息

#  研究第一个仓库
repo_dict = repo_dicts[0]       # 为更深入地了解返回的有关每个仓库的信息，我们提取了 repo_dicts 中的第一个字典，并将其存储在 repo_dict 中
print("\nKeys:", len(repo_dict))        # 接下来，我们打印这个字典包含的键数，看看其中有多少信息
for key in sorted(repo_dict.keys()):        # 我们打印这个字典的所有键，看看其中包含哪些信息
    print(key)