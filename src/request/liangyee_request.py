#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request

user_key = "c7f86ed094ad40f285c4a2f9323b85e0"
hliangyee_query_url = "http://stock.liangyee.com/bus-api/"

# 上市公司财务数据
def query_fundamental(code):
    url = hliangyee_query_url + "corporateFinance/stockFinance/GetStockList?userKey={}&symbol={}"
    url = url.format(user_key, code)
    print(url)
    try:
        data = urllib.request.urlopen(url).read()
        data = data.decode("utf8")
        return data[14: -3].split("~")
    except Exception as e:
        print("error:", e)

if __name__ == "__main__":
    code = "600519"
    print(query_fundamental(code))
