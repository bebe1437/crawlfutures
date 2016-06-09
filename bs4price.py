# encoding: utf-8

from bs4 import BeautifulSoup

m_index = 2
h_index = 4
l_index = 5
d_index = 6
u_index = 11

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

                    output = [contract, highest_price, lowest_price, closed_price, unclosed_contract]
                    if contract and not ("W" in contract):
                        return output
                        break
                    data = []
                cnt = cnt + 1
    return []
