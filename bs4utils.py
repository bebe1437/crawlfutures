# encoding: utf-8

from bs4 import BeautifulSoup

import bs4price, bs4tenfive, bs4comp, bs4taiex
import os.path

m_index = 2
h_index = 4
l_index = 5
d_index = 6
u_index = 11
filename = "futures.csv"

def write(price_html, tenfive_html, comp_html, taiex_html, date):
    if not os.path.isfile(filename):
        with open(filename, "w") as f:
            titles =["date","taiex","contract","high","low","price","unclosed","5bull", "5bear", "10bull", "10bear","CompBull", "CompBear"]
            #titles =["日期","契約","最高","最低","價格","未平倉口數","5大多", "5大空", "10大多", "10大空"]
            title = ",".join(titles)+"\n"
            print title
            f.write(title)
    price = bs4price.parse(price_html)
    if len(price) >0:
        tenfive= bs4tenfive.parse(tenfive_html)
        comp = bs4comp.parse(comp_html)
        taiex = bs4taiex.parse(taiex_html)
        data =[date, taiex] + price + tenfive+comp
        with open(filename, 'a') as f:
            line = ",".join(data)+"\n"
            print line
            f.write(line)
