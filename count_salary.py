# -*- coding:utf-8 -*-

from mysqldb import DB
import re
import collections

class Analyse:
    def deal_result(self,result):
        anl = Analyse()
        dis = []
        for res in result:
            str_new = re.findall(r"\d*", res[0])
            str_all = anl.deal_str(str_new)
            deal_all = anl.deal_all(str_all)
            for new in deal_all:
                if new != '':
                    dis.append(new)
        return dis
#处理元组中为空的
    def deal_str(self,str_new):
        new = []
        for str in str_new:
            if str != '':
                new.append(str)
        return new
#生成要处理的数组
    def deal_all(self,str_all):
        return range(int(str_all[0]),int(str_all[1])+1,1)


if __name__ == "__main__":
    db = DB()
    result = db.get_salary()
    anl = Analyse()
    salary = anl.deal_result(result)
    d = collections.Counter(salary)
    for a in d:
        print str(a)+":"+str(d[a])

