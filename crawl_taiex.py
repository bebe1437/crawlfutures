# encoding: utf-8

from bs4 import BeautifulSoup
from urlib2crawl import crawl
import os.path, datetime, sys, calendar, random, time

url = "http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX.php"
table_index = 4
taiex_index = 7

def process(year, month, day):
    rocdate = "%d/%02d/%02d" %(year-1911, month, day)
    form_data = {
        "selectType": "MS", 
        "qdate":rocdate
    }
    html = crawl(url, form_data)
    data = parse(html)
    if data:
        write(data, year, month, day)

def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    #print soup.prettify()
    tables = soup.table
    table = get(tables)
    if table:
        cnt = 1
        for child in table.descendants:
            if "td" == child.name:
                if taiex_index == cnt:
                    taiex = child.text.strip().replace(",","").split(".")[0]
                    return taiex
                cnt = cnt +1                


def get(tables):
    if tables:
        cnt = 1
        for table in tables:
            if cnt == table_index:
                return table
            cnt = cnt +1

titles =['date','price']

def write(data, year, month, day):
    filename = "taiex.csv"
    if not os.path.isfile(filename):
        with open(filename, "w") as f:
            title = ",".join(titles)+"\n"
            print title
            f.write(title)
 
    dates = "%d/%02d/%02d" % (year, month, day)
    datas = [dates, data]
    with open(filename, "a") as f:
        line = ",".join(datas)+"\n"
        print line
        f.write(line)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        arg = sys.argv[1].split('/')
        if len(arg) == 3:
            year = int(arg[0])
            month = int(arg[1])
            day = int(arg[2])
            print "crawling data of %d/%02d/%02d" % (year, month, day)
            process(year, month, day)
    elif len(sys.argv) == 4:
        year_index = 1
        month_s_index = 2
        month_e_index = 3
        
        year = int(sys.argv[year_index])
        month_s = int(sys.argv[month_s_index])
        month_e = int(sys.argv[month_e_index])
        print "crawling data of %s/%s~%s" % ( year, month_s, month_e)

        month_e = month_e + 1
        for month in range(month_s, month_e):
            last_day = calendar.monthrange(year, month)[1]
            for day in range(1, last_day):
                process(year, month, day)
                #sleep randomly from 0.5 sec to 1 sec
                time.sleep(random.uniform(0.5, 1))
