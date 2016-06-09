# encoding: utf-8

from bs4 import BeautifulSoup

table_index = 4
taiex_index = 7

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

