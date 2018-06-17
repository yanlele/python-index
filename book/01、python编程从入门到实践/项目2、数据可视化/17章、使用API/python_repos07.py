# -*- coding: utf-8 -*-
__author__ = 'YanLe'

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储相应
URL = 'https://api.github.com/search/repositories?q=language:python&sort=star'
r = requests.get(URL)
print('Status Code', r.status_code)

# 把相应存储到一个变量中去
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

#  研究有关仓库的信息
repo_dicts = response_dict['items']
print("Number of items:", len(repo_dicts))
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    if repo_dict['description']:
        plot_dict = {'value': repo_dict['stargazers_count'],
                     'label': repo_dict['description'],
                     'xlink': repo_dict['html_url']
                     }
    else:
        plot_dict = {'value': repo_dict['stargazers_count'],
                     'label': '',
                     'xlink': repo_dict['html_url']}
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()      # 我们创建了一个 Pygal 类 Config 的实例，并将其命名为 my_config 。通过修改 my_config 的属性，可定制图表的外观。
my_config.x_label_rotation = 45     # x_label_rotation 和 show_legend ，它们原来是在创建 Bar 实例时以关键字实参的方式传递的
my_config.show_legend = False
my_config.title_font_size = 24      # 我们设置了图表标题、副标签和主标签的字体大小
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15       # 用 truncate_label 将较长的项目名缩短为 15 个字符
my_config.show_y_guides = False     # 我们将 show_y_guides 设置为 False，以隐藏图表中的水平线
my_config.width = 1000              # 处设置了自定义宽度，让图表更充分地利用浏览器中的可用空间。

chart = pygal.Bar(my_config, style=my_style)        # 处创建 Bar 实例时，我们将 my_config 作为第一个实参，从而通过一个实参传递了所有的配置设置。
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
