"""给图表区域着色
添加两个数据系列后，我们就可以了解每天的气温范围了。
下面来给这个图表做最后的修饰，通过着色来呈现每天的气温范围。
为此，我们将使用方法 fill_between() ，它接受一个 x  值系列和两个 y  值系列，并填充两个 y  值系列之间的空间
"""

import csv
from datetime import datetime
from matplotlib import pyplot as plt

# 从文件中获取最高气温
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # 这个就是读取的头部信息

    dates, highs, lows = [], [], []       # 我们创建了两个空列表，用于存储从文件中提取的日期和最高气温，我们添加了空列表 lows ，用于存储最低气温
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")        # 我们将包含日期信息的数据（ row[0] ）转换为 datetime 对象
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)        # 下面使用 int() 将这些字符串转换为数字，让 matplotlib 能够读取它们

        low = int(row[3])       # 我们从每行的第 4 列（ row[3] ）提取每天的最低气温，并存储它们
        lows.append(low)

#  根据数据绘制图形
fig = plt.figure(dpi=128,figsize=(10,6))        # 设置绘图窗口的尺寸
# 处的实参 alpha 指定颜色的透明度。 Alpha 值为 0 表示完全透明， 1 （默认设置）表示完全不透明。通过将 alpha 设置为 0.5 ，可让红色和蓝色折线的颜色看起来更浅。
plt.plot(dates, highs, c='red', alpha=0.5)     # 我们将日期和最高气温值传递给 plot()
plt.plot(dates, lows, c='blue', alpha=0.5)     # 我们添加了一个对 plot() 的调用，以使用蓝色绘制最低气温
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)       # 我们向 fill_between() 传递了一个 x  值系列：列表 dates ，还传递了两个 y  值系列： highs 和 lows 。实参 facecolor 指定了填充区域的颜色，我们还将 alpha设置成了较小的值 0.1 ，让填充区域将两个数据系列连接起来的同时不分散观察者的注意力。

# 设置图形的格式
plt.title("Daily high and low temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()     # 我们调用了 fig.autofmt_xdate() 来绘制斜的日期标签，以免它们彼此重叠
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()