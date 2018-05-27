"""打印文件头及其位置"""
import csv
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)       # 这个就是读取的头部信息

    for index, column_header in enumerate(header_row):      # 对列表调用了enumerate()来获取每个元素的索引及其值。
        print(index, column_header)