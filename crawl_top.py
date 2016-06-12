# encoding: utf-8

from bs4 import BeautifulSoup
from urlib2crawl import crawl
import os.path, datetime, sys, calendar, random, time


url = "https://www.taifex.com.tw/chinese/3/7_8.asp"

contract_index = 1
amt5_bull_index = 2
amt10_bull_index = 4
amt5_bear_index = 6
amt10_bear_index = 8
market_index = 10

range_index = 10

def process(year, month, day):
    form_data = {
        "chooseitemtemp": "TX",
        "yytemp": year,
        "mmtemp":month,
        "ddtemp":day,
        "choose_yy":year,
        "choose_mm":month,
        "choose_dd":day
    }    
    html = crawl(url, form_data)
    data = parse(html)
    if data:
        write(data, year, month, day)

def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    #print soup.prettify()
    tables = soup.find("table", class_="table_f")

    if tables:
        cnt = -1
        rows = []
        data = []
        for child in tables.descendants:
            if "td"== child.name:
                cnt = cnt + 1
                if cnt == 0:
                    pass
                else:
                    content = child.text.encode("utf-8").strip()
                    data.append(content)
                    if cnt == range_index:
                        #print data
                        amt5Bull = data[amt5_bull_index-1].split("(")[0].replace(",","")
                        amt5Bear = data[amt5_bear_index-1].split("\r\n")[0].replace(",","")
                        amt10Bull = data[amt10_bull_index-1].split("\r\n")[0].replace(",","")
                        amt10Bear = data[amt10_bear_index-1].split("\r\n")[0].replace(",","")
                        amtMarket = data[market_index-1].replace(",","")
                        amt = [amt5Bull, amt5Bear, amt10Bull, amt10Bear,amtMarket]
                        rows.append(amt)
                        cnt = 0
                        data = []
        return rows[1]+rows[2]
    return []

titles =['date'"t5Bull", "t5Bear","t10Bull","t10Bear","market"]

def write(data, year, month, day):
    filename = "top.csv"
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
        print "crawling data of %s/%s~%s" % (year, month_s, month_e)

        month_e = month_e+1
        for month in range(month_s, month_e):
            last_day = calendar.monthrange(year, month)[1]
            for day in range(1, last_day):
                process(year, month, day)
                #sleep randomly from 0.5 sec to 1 sec
                time.sleep(random.uniform(0.5, 1))
