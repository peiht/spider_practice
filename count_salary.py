# -*- coding:utf-8 -*-

from mysqldb import DB
import re

class Analyse:
    def deal_result(self,result):
        dis = []
        for res in result:
            str_new = re.findall(r"\d*", res[0])
            for new in str_new:
                if new != '':
                    dis.append(new)
        return dis

if __name__ == "__main__":
    db = DB()
    result = db.get_salary()
    anl = Analyse()
    salary = anl.deal_result(result)
    print salary

