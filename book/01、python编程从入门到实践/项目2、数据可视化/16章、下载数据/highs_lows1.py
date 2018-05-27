"""分析 CSV 文件头"""
import csv
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)       # 这个就是读取的头部信息
    print(header_row)