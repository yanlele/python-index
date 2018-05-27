"""再绘制一个数据系列,在其中再添加最低气温数据"""
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
plt.plot(dates, highs, c='red')     # 我们将日期和最高气温值传递给 plot()
plt.plot(dates, lows, c='blue')     # 我们添加了一个对 plot() 的调用，以使用蓝色绘制最低气温

# 设置图形的格式
plt.title("Daily high and low temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()     # 我们调用了 fig.autofmt_xdate() 来绘制斜的日期标签，以免它们彼此重叠
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()