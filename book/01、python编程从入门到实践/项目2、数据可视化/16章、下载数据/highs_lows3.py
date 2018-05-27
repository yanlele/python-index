"""从文件中获取最高气温"""
import csv

# 从文件中获取最高气温
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # 这个就是读取的头部信息

    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)        # 下面使用 int() 将这些字符串转换为数字，让 matplotlib 能够读取它们

    print(highs)
