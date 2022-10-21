from mpl_toolkits import axisartist
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# python里的很多包会自作聪明的帮你加载各种样式，因此先整个新的画布
fig = plt.figure()
# 创建一个绘图区对象，用于调整坐标轴
ax = axisartist.Subplot(fig, 111)
# 添加绘图区对象到画布中，这里没报错很神奇，不理解，无限套娃？
fig.add_axes(ax)
# 坐标轴加上方向箭头
ax.axis["bottom"].set_axisline_style("->", size=1.5)
ax.axis["left"].set_axisline_style("->", size=1.5)
ax.axis["top"].set_visible(False)
ax.axis["right"].set_visible(False)
ax.set_xlim(-10, 10)
ax.set_xticks(range(-10, 10))

# 正态分布N（-3，4）抽样
X = np.random.normal(loc=-3, scale=2, size=(1, 10000))[0]
# print(X)
# 正态分布N（2，4）抽样
Y = np.random.normal(loc=2, scale=2, size=(1, 10000))[0]
# print(Y)
# 在均匀分布U（0，1）之间抽样
P = np.random.uniform(0, 1, size=(1, 10000))[0]
# print(P)

Z = P * X + (1 - P) * Y

sns.distplot(Z, bins=100, hist=True, kde=True)

# 模拟计算0.9的分位数
fen_wei = np.percentile(Z, 90)
# print(fen_wei)

# 求方差
Z_var = np.var(Z)
# 求均值
Z_mean = np.mean(Z)
# print(Z_var)
# print(Z_mean)

plt.text(5, 0.175, '方差:{:.3f}'.format(Z_var),
         family='FangSong', verticalalignment='center', color='#6495ED', fontsize=15)
plt.text(5, 0.1625, '期望:{:.3f}'.format(Z_mean),
         family='FangSong', verticalalignment='center', color='#6495ED', fontsize=15)
plt.text(5, 0.15, '0.9分位值:{:.3f}'.format(fen_wei),
         family='FangSong', verticalalignment='center', color='#6495ED', fontsize=15)
plt.show()
