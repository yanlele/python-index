"""
使用颜色映射 和 自动保存图表
颜色映射 （ colormap ）是一系列颜色，它们从起始颜色渐变到结束颜色。
"""
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# 但绘制很多点时，黑色轮廓可能会粘连在一起。要删除数据点的轮廓，可在调用 scatter() 时传递实参 edgecolor='none'
# 可传递参数 c ，并将其设置为一个元组，其中包含三个 0~1 之间的小数值，它们分别表示红色、绿色和蓝色分量。
# 我们将参数 c 设置成了一个 y  值列表，并使用参数 cmap 告诉 pyplot 使用哪个颜色映射。这些代码将 y  值较小的点显示为浅蓝色，并将 y  值较大的点显示为深蓝色
plt.scatter(x_values, y_values,c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

#  设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#  设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

#  设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

# 要让程序自动将图表保存到文件中，可将对 plt.show() 的调用替换为对 plt.savefig() 的调用
plt.savefig('squares_plot.png', bbox_inches='tight')