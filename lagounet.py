# coding:utf-8

import urllib2
from bs4 import BeautifulSoup
from mysqldb import DB
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class Spider:

    def deal_url(self,url):
        if url is None:
            return None
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:52.0) Gecko/20100101 Firefox/52.0",
            "Cookie": "Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1466075280; __utma=194070582.826403744.1466075281.1466075281.1466075281.1; __utmv=194070582.|2=User%20Type=Visitor=1; signin_redirect=http%3A%2F%2Fwww.jianshu.com%2Fsearch%3Fq%3D%25E7%2594%259F%25E6%25B4%25BB%26page%3D1%26type%3Dnote; _session_id=ajBLb3h5SDArK05NdDY2V0xyUTNpQ1ZCZjNOdEhvNUNicmY0b0NtMnVuUUdkRno2emEyaFNTT3pKWTVkb3ZKT1dvbTU2c3c0VGlGS0wvUExrVW1wbkg1cDZSUTFMVVprbTJ2aXhTcTdHN2lEdnhMRUNkM1FuaW1vdFpNTDFsQXgwQlNjUnVRczhPd2FQM2sveGJCbDVpQUVWN1ZPYW1paUpVakhDbFVPbEVNRWZzUXh5R1d0LzE2RkRnc0lJSHJEOWtnaVM1ZE1yMkt5VC90K2tkeGJQMlVOQnB1Rmx2TFpxamtDQnlSakxrS1lxS0hONXZnZEx0bDR5c2w4Mm5lMitESTBidWE4NTBGNldiZXVQSjhjTGNCeGFOUlpESk9lMlJUTDVibjNBUHdDeVEzMGNaRGlwYkg5bHhNeUxJUVF2N3hYb3p5QzVNTDB4dU4zODljdExnPT0tLU81TTZybUc3MC9BZkltRDBiTEsvU2c9PQ%3D%3D--096a8e4707e00b06b996e8722a58e25aa5117ee9; CNZZDATA1258679142=1544596149-1486533130-https%253A%252F%252Fwww.baidu.com%252F%7C1486561790; _ga=GA1.2.826403744.1466075281; _gat=1",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
        }
        content = ""
        try:
            request = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(request)
            response.encoding = 'utf-8'
            content = response.read()
        except urllib2.URLError, e:
            if hasattr(e, "reason") and hasattr(e, "code"):
                print e.code
                print e.reason
            else:
                print "请求失败"
        return content

    def parse(self,soup):
        list = []
        lips = soup.find_all('li', class_='con_list_item default_list')
        for lip in lips:
            data = {}
            salary = lip.find('span', {'class': 'money'})
            # print salary.text
            company = lip.find('div', {'class': 'company_name'})
            require = lip.find('div', {'class': 'li_b_l'})
            job = lip.find('h3')
            address = lip.find('em')
            data['job'] = job.text
            data['address'] = address.text
            data['require'] = require.text
            data['company'] = company.text
            list.append(data)
        return list


if __name__ =="__main__":
    root_url = "https://www.lagou.com/zhaopin/Java/?labelWords=label"
    spider = Spider()
    content = spider.deal_url(root_url)
    soup = BeautifulSoup(content, "html.parser", from_encoding="utf-8")
    datas = spider.parse(soup)
    db = DB()
    for data in datas:
        print type(data['job'])
        #db.importDb(data['job'],data['address'],data['require'],data['company'])

