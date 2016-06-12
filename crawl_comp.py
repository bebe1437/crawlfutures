# encoding: utf-8

from bs4 import BeautifulSoup
from urlib2crawl import crawl
import os.path, datetime, sys, calendar, random, time

url = "https://www.taifex.com.tw/chinese/3/7_12_3.asp"
bull_index=2
bear_index=4
bull_unclosed_index=8
bear_unclosed_index=10

index = 13
rows_len = 3

def process(cid, year, month, day):
    form_data = {
        "commodity_id": cid,
        "DATA_DATE_Y": year,
        "DATA_DATE_M":month,
        "DATA_DATE_D":day,
        "syear":year,
        "smonth":month,
        "sday":day
    }
    html = crawl(url, form_data)
    data = parse(html)
    if data :
        write(data, cid, year, month, day)

def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    #print soup.prettify()
    tables = soup.find("table", class_="table_f")

    if tables:
        cnt = -2
        data = []
        rows = []
        for child in tables.descendants:
            if "td"== child.name:
                cnt = cnt + 1
                if cnt > 0:
                    content = child.text.encode("utf-8").strip()
                    data.append(content)
                if cnt == index:
                    bull = data[bull_index-1].replace(",","")
                    bear = data[bear_index-1].replace(",","")
                    bull_unclosed = data[bull_unclosed_index-1].replace(",","")
                    bear_unclosed = data[bear_unclosed_index-1].replace(",","")
                    rows.append([bull,bear,bull_unclosed,bear_unclosed])
                    data =[]
                    cnt = 0
                    if len(rows)==rows_len:
                        break
        return rows[0]+rows[1]+rows[2]
    return []


titles =['date'
        ,"dealer_dealed_bull", "dealer_dealed_bear","dealer_bull","dealer_bear"
        ,"trust_dealed_bull", "trust_dealed_bear","trust_bull","trust_bear"
        ,"foreign_dealed_bull", "foreign_dealed_bear","foreign_bull","foreign_bear"]

def write(data, cid, year, month, day):
    filename = "unclosed_%s.csv" % (cid)
    if not os.path.isfile(filename):
        with open(filename, "w") as f:
            title = ",".join(titles)+"\n"
            print title
            f.write(title)
 
    dates = "%d/%02d/%02d" % (year, month, day)
    datas = [dates] + data
    with open(filename, "a") as f:
        line = ",".join(datas)+"\n"
        print line
        f.write(line)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        arg = sys.argv[2].split('/')
        if len(arg) == 3:
            cid = sys.argv[1]
            year = int(arg[0])
            month = int(arg[1])
            day = int(arg[2])
            print "crawling data[%s] of %d/%02d/%02d" % (cid, year, month, day)
            process(cid, year, month, day)     
    elif len(sys.argv) == 5:
        cid_index = 1
        year_index = 2
        month_s_index = 3
        month_e_index = 4        
        cid = sys.argv[cid_index]
        year = int(sys.argv[year_index])
        month_s = int(sys.argv[month_s_index])
        month_e = int(sys.argv[month_e_index])
        print "crawling data[%s] of %s/%s~%s" % (cid, year, month_s, month_e)

        month_e = month_e +1
        for month in range(month_s, month_e):
            last_day = calendar.monthrange(year, month)[1]
            for day in range(1, last_day):
                process(cid, year, month, day)
                #sleep randomly from 0.5 sec to 1 sec
                time.sleep(random.uniform(0.5, 1))
