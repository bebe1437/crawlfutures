# encoding: utf-8

from bs4 import BeautifulSoup

bull_index = 88
bear_index = 90

def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    #print soup.prettify()
    tables = soup.find("table", class_="table_f")

    if tables:
        cnt = 0
        bull = 0
        bear =0
        for child in tables.descendants:
            if "td"== child.name:
                if cnt == bull_index:
                    bull = child.text.encode("utf-8").strip().replace(",","")
                elif cnt == bear_index:
                    bear = child.text.encode("utf-8").strip().replace(",","")
                cnt = cnt +1
        return [bull, bear]
    return []
