# encoding: utf-8

from bs4 import BeautifulSoup

contract_index = 1
amt5_bull_index = 2
amt10_bull_index = 4
amt5_bear_index = 6
amt10_bear_index = 8
market_index = 10

def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    #print soup.prettify()
    tables = soup.find("table", class_="table_f")

    if tables:
        cnt = 0
        data = []
        for child in tables.descendants:
            if "td"== child.name:
                if cnt != 0:
                    #print "[",cnt,"]", child.text.strip()
                    str = child.text.encode("utf-8").strip()
                    data.append(str)
                cnt = cnt + 1
                if cnt == 11:
                    if "所有契約" == data[0]:
                        amt5Bull = data[amt5_bull_index-1].split("(")[0].replace(",","")
                        amt5Bear = data[amt5_bear_index-1].split("\r\n")[0].replace(",","")
                        amt10Bull = data[amt10_bull_index-1].split("\r\n")[0].replace(",","")
                        amt10Bear = data[amt10_bear_index-1].split("\r\n")[0].replace(",","")
                        return [amt5Bull, amt5Bear, amt10Bull, amt10Bear]
                    cnt = 1
                    data = []
    return []
