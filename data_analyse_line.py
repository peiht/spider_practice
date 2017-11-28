#-*- coding:utf-8 –*-


from matplotlib.mlab import *
from matplotlib.pyplot import *
import numpy as np

#从-4到4之间取200个随机数，存到数组中
x = np.linspace(-4, 4, 200)
#power表示10的x次方
f1 = np.power(10, x)
f2 = np.power(np.e, x)
f3 = np.power(2, x)

#三个参数一组，第一个代表数据，第二个代表函数，第三个代表线的颜色，最后linewidth代表线的宽度
plot(x, f1, 'r', x, f2, 'b', x, f3, 'g', linewidth=2)
#图的坐标，左右和下上
axis([-4, 4, -0.5, 8])
#显示字体的位置和大小
text(1, 7.5, r'$10^x$', fontsize=16)
text(2.2, 7.5, r'$e^x$', fontsize=16)
text(3.2, 7.5, r'$2^x$', fontsize=16)
title('A simple example', fontsize=16)

#保存的设置。保存的文件名和分辨率
savefig('power.png', dpi=75)
show()