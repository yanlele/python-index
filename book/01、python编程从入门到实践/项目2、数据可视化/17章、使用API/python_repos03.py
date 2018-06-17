# -*- coding: utf-8 -*-
"""
提取 repo_dict 中与一些键相关联的值
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
print("\nSelected information about first repository:")
print('Name:', repo_dict['name'])       # 打印了项目的名称
print('Owner:', repo_dict['owner']['login'])        # 表示所有者的字典，再使用键 key 来获取所有者的登录名
print('Stars:', repo_dict['stargazers_count'])      # 打印项目获得了多少个星的评级,以及项目在 GitHub 仓库的 URL
print('Repository:', repo_dict['html_url'])     # 仓库的url
print('Created:', repo_dict['created_at'])      # 创建时间
print('Updated:', repo_dict['updated_at'])      # 最后一次更新时间
print('Description:', repo_dict['description'])     # 描述信息