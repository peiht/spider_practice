# coding:utf-8

import MySQLdb
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
class DB:
    conn = MySQLdb.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='root',
        db='spider'
    )

    def importDb(self,job_name,job_address,job_require,job_company):
        conn = self.conn
        cur = conn.cursor()
        cur.execute("insert into job values(null,"+job_name+","+job_address+","+job_require+","+job_company+")")
        # result = cur.execute("select * from job")
        # print result
        # info = cur.fetchmany(result)
        # for infos in info:
        #     for job in infos:
        #         print job
        cur.close()
        conn.commit()
        conn.close()

