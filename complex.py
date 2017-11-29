#-*- coding:utf-8 –*-
import re

string = '20k-30k'
str_new = re.findall(r"\d*",string)
#str_new = filter(str.isdigit(string),string)
dis = []
for new in str_new:
    if new != '':
        dis.append(new)
print dis

a = int(dis[0])
print a
b = int(dis[1])
print b
number = range(a,b+1,1)
print number
