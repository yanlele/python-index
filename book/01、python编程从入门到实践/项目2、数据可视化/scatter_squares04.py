"""删除数据点的轮廓 || 自定义颜色"""
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# 但绘制很多点时，黑色轮廓可能会粘连在一起。要删除数据点的轮廓，可在调用 scatter() 时传递实参 edgecolor='none'
# 可传递参数 c ，并将其设置为一个元组，其中包含三个 0~1 之间的小数值，它们分别表示红色、绿色和蓝色分量。
plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)

#  设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#  设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

#  设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])


plt.show()