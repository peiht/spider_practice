# coding:utf-8

import MySQLdb
class DB:

    #定义数据入库的函数
    def importDb(self,job_salary,job_name,job_address,job_require,job_company):
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='root',
            db='spider',
            charset='utf8'
        )
        cur = conn.cursor()
        cur.execute("insert into job values(null,'"+job_salary+"','"+job_name+"','"+job_address+"','"+job_require+"','"+job_company+"')")
        cur.close()
        conn.commit()
        conn.close()


    def get_salary(self):
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='root',
            db='spider'
        )
        cur = conn.cursor()
        result = cur.execute("select t.job_salary from job t ")
        info = cur.fetchmany(result)
        cur.close()
        conn.commit()
        conn.close()
        return info

