# encoding: utf-8

from bs4 import BeautifulSoup
from urlib2crawl import crawl
import os.path, datetime, sys, calendar, random, time

url = "https://www.taifex.com.tw/chinese/3/3_1_1.asp"
m_index = 2
h_index = 4
l_index = 5
d_index = 6
a_index = 9
u_index = 11

def process(cid, year, month, day):
    form_data = {
        "qtype": "2", 
        "commodity_id": cid,
        "dateaddcnt": "0",
        "DATA_DATE_Y": year,
        "DATA_DATE_M":month,
        "DATA_DATE_D":day,
        "syear":year,
        "smonth":month,
        "sday":day
    }
    html = crawl(url, form_data)
    data = parse(html)
    if data:
        write(data, cid, year, month, day)
    
def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    tables = soup.find("table", class_="table_f")
    if tables:
        cnt = 1
        data = []
        for child in tables.descendants:
            if "td"== child.name:
                #print "[",cnt,"]", child.text.strip()
                data.append(child.text.strip().encode('utf-8'))
                if cnt == 15 :
                    cnt = 0
                    #print data
                    contract=data[m_index-1]
                    highest_price=data[h_index-1]
                    lowest_price=data[l_index-1]
                    closed_price=data[d_index-1]
                    unclosed_contract=data[u_index-1]
                    amount = data[a_index-1]

                    output = [contract, highest_price, lowest_price, closed_price, amount, unclosed_contract]
                    if contract and not ("W" in contract):
                        return output
                        break
                    data = []
                cnt = cnt + 1
    return []

titles =['date',"contract", "high","low","price","amount", "unclosed"]

def write(data, cid, year, month, day):
    filename = "futures_%s.csv" % (cid)
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

        month_e = month_e + 1
        for month in range(month_s, month_e):
            last_day = calendar.monthrange(year, month)[1]
            for day in range(1, last_day):
                process(cid, year, month, day)
                #sleep randomly from 0.5 sec to 1 sec
                time.sleep(random.uniform(0.5, 1))
