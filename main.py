# encoding: utf-8

from time import sleep

import bs4utils
import crawlutils
import random
import calendar
import sys
import urllib,urllib2

start_html = 0.5
end_html = 1
start_month = 1
end_month = 2

def crawling(year, month, day):
    
    price_html = crawlutils.crawl_price(year, month, day)
    tenfive_html = crawlutils.crawl_tenfive(year, month, day)
    comp_html = crawlutils.crawl_comp(year, month, day)
    taiex_html = crawlutils.crawl_taiex(year, month, day)
    
    toSleep(start_html, end_html)
    
    #output to csv file
    date = "%d/%d/%d" % (year, month, day)
    bs4utils.write(price_html, tenfive_html, comp_html, taiex_html, date)

def process(year, month_start, month_end):
    for month in range(month_start, month_end):
        last_day = calendar.monthrange(year, month)[1]
        for day in range(1, last_day):
            crawling(year, month, day)
        toSleep(start_month, end_month)

def toSleep(start, end):
    #sleep randomly from 0.5 sec to 1 sec
    sleep(random.uniform(start, end))
    
if __name__ == '__main__':
    year_index = 1
    month_s_index = 2
    month_e_index = 3
    if len(sys.argv) == 4:
        year = sys.argv[year_index]
        month_s = sys.argv[month_s_index]
        month_e = sys.argv[month_e_index]
        print "crawling data of %s/%s~%s" % (year, month_s, month_e)
        process(int(year), int(month_s), int(month_e)+1)


