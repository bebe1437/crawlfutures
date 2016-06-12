# encoding: utf-8

import urllib,urllib2

def crawl(url, form_data):
    request = urllib2.Request(url) 
    request.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36")
    form_data = urllib.urlencode(form_data)
    response = urllib2.urlopen(request,data=form_data)  
    return response.read()
    
def crawl_price(year, month, day):
    url = "https://www.taifex.com.tw/chinese/3/3_1_1.asp"
    form_data = {
        "qtype": "2", 
        "commodity_id": "MTX",
        "dateaddcnt": "0",
        "DATA_DATE_Y": year,
        "DATA_DATE_M":month,
        "DATA_DATE_D":day,
        "syear":year,
        "smonth":month,
        "sday":day
    }
    return process(url, form_data)

def crawl_tenfive(year, month, day):
    url = "https://www.taifex.com.tw/chinese/3/7_8.asp"

    form_data = {
        "chooseitemtemp": "TX",
        "yytemp": year,
        "mmtemp":month,
        "ddtemp":day,
        "choose_yy":year,
        "choose_mm":month,
        "choose_dd":day
    }
    return process(url, form_data)
    
def crawl_comp(year, month, day):
    url = "https://www.taifex.com.tw/chinese/3/7_12_3.asp"
    form_data = {
        "DATA_DATE_Y": year,
        "DATA_DATE_M":month,
        "DATA_DATE_D":day,
        "syear":year,
        "smonth":month,
        "sday":day
    }
    return process(url, form_data)

def crawl_taiex(year, month, day):
    url = "http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX.php"
    rocdate = "%d/%02d/%02d" %(year-1911, month, day)
    form_data = {
        "selectType": "MS", 
        "qdate":rocdate
    }
    return process(url, form_data)
