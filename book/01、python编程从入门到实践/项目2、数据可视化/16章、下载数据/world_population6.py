# -*- coding: utf-8 -*-
__author__ = 'YanLe'

"""使用 Pygal 设置世界地图的样式"""
import json
import pygal
from country_codes import get_country_code
from pygal.style import RotateStyle

#  将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)     # 我们首先导入了模块 json ，以便能够正确地加载文件中的数据，然后，我们将数据存储在 pop_data 中

#  创建一个包含人口数量的字典
cc_populations = {}
for pop_dict in pop_data:       # 函数 json.load() 将数据转换为 Python 能够处理的格式，这里是一个列表
    if pop_dict['Year'] == '2010':      # 们遍历 pop_data 中的每个元素。每个元素都是一个字典，包含四个键 — 值对，我们将每个字典依次存储在 pop_dict 中。
        country_name = pop_dict['Country Name']     # 如果年份为 2010 ，我们就将与 'Country Name' 相关联的值存储到 country_name 中，并将与 'Value' 相关联的值存储在 population 中
        population = int(float(pop_dict['Value']))      # 函数 float() 将字符串转换为小数，而函数 int() 丢弃小数部分，返回一个整数。现在，我们可以打印 2010 年的完整人口数据，不会导致错误了
        code = get_country_code(country_name)       # 提取国家名和人口数量后，我们将国别码存储在code 中，如果没有国别码，就在其中存储None
        if code:
            cc_populations[code] = population        # 如果返回了国别码，就保存国别码和相应国家的人口数量

#  根据人口数量将所有的国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RotateStyle('#336699')
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)
wm.render_to_file('world_population.svg')
