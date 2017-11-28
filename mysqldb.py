# coding:utf-8

import MySQLdb
class DB:



    def importDb(self,job_salary,job_name,job_address,job_require,job_company):
        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='root',
            db='spider'
        )
        cur = conn.cursor()
        cur.execute("insert into job values(null,'"+job_salary+"','"+job_name+"','"+job_address+"','"+job_require+"','"+job_company+"')")
        # result = cur.execute("select * from job")
        # print result
        # info = cur.fetchmany(result)
        # for infos in info:
        #     for job in infos:
        #         print job
        cur.close()
        conn.commit()
        conn.close()

