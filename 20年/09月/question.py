import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


###STEP2###
def convert_data_to_timeseries(input_file, column, verbose=False):
    # 导入数据
    data = np.loadtxt(input_file, delimiter=',')
    # 确定索引的开始与结束时间
    start_date = str(int(data[0, 0])) + '-' + str(int(data[0, 1]))
    end_date = str(int(data[-1, 0] + 1)) + '-' + str(int(data[-1, 1] % 12 + 1))
    ###问题一：完善函数###
    ###提示：通过pandas的date_range函数获取索引###
    dates = pd.date_range(start_date, end_date, freq='M')
    data_timeseries = pd.Series(data[:, column], index=dates)
    return data_timeseries


###STEP3###
# 文件路径
input_file = 'data.txt'
column_num = 2
data_timeseries = convert_data_to_timeseries(input_file, column_num)
# Plot方法成图
data_timeseries.plot()
plt.title('Input data')
# 图像太密集了，我们换一个时间范围
start = '2007-2'
end = '2007-11'
plt.figure()
data_timeseries[start:end].plot()
plt.title('Data from ' + start + ' to ' + end)
plt.show()

###STEP4###
###问题二：将数据的第三,四列转换为二维数据结构dataframe,索引为时间###
# 第三列
data1 = convert_data_to_timeseries(input_file, 2)
# 第四列
data2 = convert_data_to_timeseries(input_file, 3)
# 转换
dataframe = pd.DataFrame({'first': data1, 'second': data2})
# 将两组数据同时成图
dataframe['1955':'1960'].plot()
plt.title('Data overlapped on top of each other')

###STEP5###
# 查看两组数据是否有线性关联
plt.figure()
difference = dataframe['1952':'1955']['first'] - dataframe['1952':'1955']['second']
difference.plot()
plt.title('Difference (first - second)')
plt.show()

###STEP6###
###问题三：请统计两组数组的最大最小值和均值###
###问题三：计算数据的相关系数，调用corr函数###
# 最大值
print('\nMaximum:\n', dataframe.max())
# 最小值
print('\nMinimum:\n', dataframe.min())
# 平均值
print('\nMean:\n', dataframe.mean())
# 调用corr函数
print('\nCorrelation coefficients:\n', dataframe.corr())

###STEP7###
# 打印两组数据相关性
plt.figure()
pd.rolling_corr(dataframe['first'], dataframe['second'], window=60).plot()
plt.show()
