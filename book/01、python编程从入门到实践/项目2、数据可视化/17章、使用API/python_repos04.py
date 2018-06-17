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

#  概述最受欢迎的仓库
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:        # 我们遍历 repo_dicts 中的所有字典。在这个循环中，我们打印每个项目的名称、所有者、星级、在 GitHub 上的 URL 以及描述
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])