#-*- coding:utf-8 –*-
from mysqldb import DB
from count_salary import Analyse
import collections
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

db = DB()
result = db.get_salary()
anl = Analyse()
salary = anl.deal_result(result)
d = collections.Counter(salary)
#for a in d:
    #print str(a) + ":" + str(d[a])


mpl.rcParams['axes.titlesize'] = 20
mpl.rcParams['xtick.labelsize'] = 10
mpl.rcParams['ytick.labelsize'] = 16
mpl.rcParams['axes.labelsize'] = 16
mpl.rcParams['xtick.major.size'] = 0
mpl.rcParams['ytick.major.size'] = 0

# 包含了狗，猫和猎豹的最高奔跑速度，还有对应的可视化颜色
#speed_map = {
#    'dog': (48, '#7199cf'),
#    'cat': (45, '#4fc4aa'),
#    'cheetah': (120, '#e1a7a2')
#}
speed_map = {}
for s in d:
    speed_map[s] = (d[s],"#7199cf")
print speed_map.values()
# 整体图的标题
fig = plt.figure('Bar chart & Pie chart')

# 在整张图上加入一个子图，121的意思是在一个1行2列的子图中的第一张
ax = fig.add_subplot(111)
ax.set_title('Running speed - bar chart')

# 生成x轴每个元素的位置
xticks = np.arange(77)

# 定义柱状图每个柱的宽度
bar_width = 0.5

# 动物名称
animals = speed_map.keys()

# 奔跑速度
speeds = [x[0] for x in speed_map.values()]

# 对应颜色
colors = [x[1] for x in speed_map.values()]

# 画柱状图，横轴是动物标签的位置，纵轴是速度，定义柱的宽度，同时设置柱的边缘为透明
bars = ax.bar(xticks, speeds, width=bar_width, edgecolor='none')

# 设置y轴的标题
ax.set_ylabel('count')

# x轴每个标签的具体位置，设置为每个柱的中央
ax.set_xticks(xticks+bar_width/2)

# 设置每个标签的名字
ax.set_xticklabels(animals)

# 设置x轴的范围
ax.set_xlim([bar_width/2-0.5, 77-bar_width/2])

# 设置y轴的范围
ax.set_ylim([0, 310])

# 给每个bar分配指定的颜色
for bar, color in zip(bars, colors):
    bar.set_color(color)

plt.show()