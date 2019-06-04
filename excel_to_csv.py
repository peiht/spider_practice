# -*- coding:utf-8 -*-
import pandas as pd

re = pd.read_excel("D:/test.xlsx")

data = re['ee'].values

df = pd.DataFrame({'name' : data})
df.head()
df.to_csv("D:/test_csv.csv")

if __name__ == '__main__':
    print(re)
    print(data)


