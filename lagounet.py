# coding:utf-8

import urllib2
from bs4 import BeautifulSoup
from mysqldb import DB
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')

class Spider:

    def deal_url(self,url):
        if url is None:
            return None
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:52.0) Gecko/20100101 Firefox/52.0",
            "Cookie":"sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2215fb9e6691c4d4-08cdc28985e649-7b1f3c-2073600-15fb9e6691d387%22%2C%22%24device_id%22%3A%2215fb9e6691c4d4-08cdc28985e649-7b1f3c-2073600-15fb9e6691d387%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fs%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_utm_source%22%3A%22baidupc%22%2C%22%24latest_utm_medium%22%3A%22cpc%22%2C%22%24latest_utm_campaign%22%3A%22%E5%93%81%E7%89%8C%E8%AF%8D%22%2C%22%24latest_utm_term%22%3A%22bj103474%22%7D%7D; user_trace_token=20171114173957-c7081cfe-c91f-11e7-98ca-5254005c3644; LGUID=20171114173957-c7082134-c91f-11e7-98ca-5254005c3644; ab_test_random_num=0; JSESSIONID=ABAAABAAAGGABCB22417EAA04C0748133CFB8606BD1089C; X_HTTP_TOKEN=71d30b4b90f20f279c2f14eeac3e84d8; _putrc=88525859F3C7BFDD; login=true; unick=%E8%A3%B4%E6%B5%B7%E6%B6%9B; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; TG-TRACK-CODE=index_navigation; _gid=GA1.2.57041000.1511144413; _gat=1; _ga=GA1.2.445158121.1510652435; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1511333705,1511335053,1511335058,1511341146; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1511343210; LGSID=20171122165905-645fe947-cf63-11e7-9d25-525400f775ce; LGRID=20171122173329-32bc8994-cf68-11e7-9986-5254005c3644; SEARCH_ID=940522d5512947fcac5afe0d9b447729; index_location_city=%E5%85%A8%E5%9B%BD",
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
            data['job'] = job.text.encode('utf-8').strip()
            data['address'] = address.text.encode('utf-8').strip()
            job_require = require.text.encode('utf-8').strip()
            data['salary'] = job_require.split('\n')[0]
            data['require'] = job_require.split('\n')[1]
            #data['require'] = require.text.encode('utf-8').strip()
            data['company'] = company.text.encode('utf-8').strip()
            list.append(data)
        return list

    def get_more_url(self,soup):
        links = soup.find_all('div',class_='pager_container')
        list = []
        list.append('https://www.lagou.com/zhaopin/Java/?labelWords=label')
        for link in links:
            href = link.find('a',{'class':'page_no','data-index':'2'})
            url = href['href'].encode('utf-8')
            for n in range(2,31):
                new_url = url[:35] + str(n)+'/'
                list.append(new_url)
        return list



if __name__ =="__main__":
    root_url = "https://www.lagou.com/zhaopin/Java/?labelWords=label"
    spider = Spider()
    content = spider.deal_url(root_url)
    soup = BeautifulSoup(content, "html.parser", from_encoding="utf-8")
    lists = spider.get_more_url(soup)
    for list in lists:
        content = spider.deal_url(list)
        print '正在爬取的链接:' + list
        soup = BeautifulSoup(content, "html.parser", from_encoding="utf-8")
        #print soup
        datas = spider.parse(soup)
        #print datas
        db = DB()
        for data in datas:
            print data['salary']
            db.importDb(data['salary'],data['job'],data['address'],data['require'],data['company'])

