"""绘制气温图表"""
import csv
from matplotlib import pyplot as plt

# 从文件中获取最高气温
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # 这个就是读取的头部信息

    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)        # 下面使用 int() 将这些字符串转换为数字，让 matplotlib 能够读取它们

#  根据数据绘制图形
fig = plt.figure(dpi=128,figsize=(10,6))        # 设置绘图窗口的尺寸
plt.plot(highs, c='red')

# 设置图形的格式
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()