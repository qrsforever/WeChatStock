#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
import re

tencent_query_url = "http://qt.gtimg.cn"

def request_stock_list():
    URL = "http://quote.eastmoney.com/stocklist.html"
    stock_list = []
    html = urllib.request.urlopen(URL).read()
    html = html.decode("gbk")
    s = r'<li><a target="_blank" href="http://quote.eastmoney.com/.*.html">(?P<name>\w+)\((?P<code>\d+)\)'
    pat = re.compile(s)
    code = pat.findall(html)
    for item in code:
        if item[1][0] =='6' or item[1][0] =='3' or item[1][0]=='0':
            stock_list.append(item)
    return stock_list

def request_stock_data(codes, start, end):
    URL = "http://quotes.money.163.com/service/chddata.html"
    FIELDS = "TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
    for code in codes:
        print(code)
        url = URL
        if code[0] == '6':
            url += "?code=0" + code
        else:
            url += "?code=1" + code
        url += "&start=" + start + "&end=" + end + "&fields=" + FIELDS

        data = urllib.request.urlopen(url).read()
        yield data.decode("gbk")

def request_stock_data_by(code, field, start = "20100101", end = "20190101"):
    URL = "http://quotes.money.163.com/service/chddata.html"
    FIELDS = ("TCLOSE","HIGH","LOW","TOPEN","LCLOSE","CHG","PCHG","TURNOVER","VOTURNOVER","VATURNOVER","TCAP","MCAP")
    txt = field.upper()
    if txt not in FIELDS:
        return None
    print(code)
    url = URL
    if code[0] == '6':
        url += "?code=0" + code
    else:
        url += "?code=1" + code
    url += "&start=" + start + "&end=" + end + "&fields=" + txt
    print(url)
    data = urllib.request.urlopen(url).read()
    return data.decode("gbk")

# 获取最新行情
def request_latest_quotation(code):
    url = tencent_query_url + "/q=" + ("sh" if code[0] == "6" else "sz") + code
    try:
        data = urllib.request.urlopen(url).read()
        data = data.decode("gbk")
        return data[12: -3].split("~")
    except Exception as e:
        print("error:", e)

    return None

# 获取实时资金流向
def request_money_flow(code):
    url = tencent_query_url + "/q=ff_" + ("sh" if code[0] == "6" else "sz") + code
    try:
        data = urllib.request.urlopen(url).read()
        data = data.decode("gbk")
        return data[15: -3].split("~")
    except Exception as e:
        print("error:", e)

    return None

# 获取盘口分析
def request_dish_mouth(code):
    url = tencent_query_url + "/q=s_pk" + ("sh" if code[0] == "6" else "sz") + code
    try:
        data = urllib.request.urlopen(url).read()
        data = data.decode("gbk")
        return data[16: -3].split("~")
    except Exception as e:
        print("error:", e)

    return None

# 获取简要信息
def request_brief_info(code):
    url = tencent_query_url + "/q=s_" + ("sh" if code[0] == "6" else "sz") + code
    try:
        data = urllib.request.urlopen(url).read()
        data = data.decode("gbk")
        return data[14: -3].split("~")
    except Exception as e:
        print("error:", e)

    return None

if __name__ == "__main__":
    code = "600519"
    try:
        #  request_stock_list()
        print (request_stock_data_by(code, "turnover"))
    except Exception as e:
        print("error:", e)
    #  print(request_latest_quotation(code))
    #  print(request_money_flow(code))
    #  print(request_dish_mouth(code))
    #  print(request_brief_info(code))

