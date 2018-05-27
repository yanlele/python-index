"""绘制直方图: 掷几次骰子，并将结果存储在一个列表中 | 分析结果-计算每个点数出现的次数"""
from die import Die
import pygal

# 创建一个D6骰子
die = Die()

#  掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果-计算每个点数出现的次数
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()  # 为创建条形图，我们创建了一个 pygal.Bar() 实例，并将其存储在 hist 中

hist.title = 'D6 骰子投掷1000次'
hist.x_labels = ['1', '2', '3', '4', '5', '6']  # 我们设置 hist 的属性 title （用于标示直方图的字符串），将掷 D6 骰子的可能结果用作 x  轴的标签
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6', frequencies)     # 给每个轴都添加了标题

# 最后，我们将这个图表渲染为一个 SVG 文件，这种文件的扩展名必须为 .svg， 要查看生成的直方图，最简单的方式是使用 Web 浏览器。
hist.render_to_file('die_visual.svg')