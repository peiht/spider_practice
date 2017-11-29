#-*- coding:utf-8 –*-

import numpy as np
import collections

lst = [1,1,1,1,2,2,2,2,4,4,4,4,46,6,5,6,6,6]

d = collections.Counter(lst)

for a in d:
    print str(a) +":"+ str(d[a])