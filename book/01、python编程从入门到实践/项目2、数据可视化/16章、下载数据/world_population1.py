"""提取相关的数据"""

import json
#  将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)     # 我们首先导入了模块 json ，以便能够正确地加载文件中的数据，然后，我们将数据存储在 pop_data 中

# 打印每个国家2010年的人口数量
for pop_dict in pop_data:       # 函数 json.load() 将数据转换为 Python 能够处理的格式，这里是一个列表
    if pop_dict['Year'] == '2010':      # 们遍历 pop_data 中的每个元素。每个元素都是一个字典，包含四个键 — 值对，我们将每个字典依次存储在 pop_dict 中。
        country_name = pop_dict['Country Name']     # 如果年份为 2010 ，我们就将与 'Country Name' 相关联的值存储到 country_name 中，并将与 'Value' 相关联的值存储在 population 中
        population = pop_dict['Value']
        print(country_name + ': ' + population)


