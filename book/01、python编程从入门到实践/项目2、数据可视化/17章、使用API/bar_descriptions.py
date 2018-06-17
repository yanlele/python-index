# -*- coding: utf-8 -*-
"""
添加自定义工具提示
在 Pygal 中，将鼠标指向条形将显示它表示的信息，这通常称为 工具提示 。在这个示例中，当前显示的是项目获得了多少个星。下面来创建一个自定义工具提示，以同时显示项目的描述。
来看一个简单的示例，它可视化前三个项目，并给每个项目对应的条形都指定自定义标签。为此，我们向 add() 传递一个字典列表，而不是值列表：
"""
__author__ = 'YanLe'


import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
    {'value': 16101, 'label': 'Description of httpie.'},
    {'value': 15028, 'label': 'Description of django.'},
    {'value': 14798, 'label': 'Description of flask.'},
]

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
