#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
import re

def request_stock_codes():
    URL = "http://quote.eastmoney.com/stocklist.html"
    code_list = []
    html = urllib.request.urlopen(URL).read()
    html = html.decode("gbk")
    # \S\S: sh and sz
    s = r'<li><a target="_blank" href="http://quote.eastmoney.com/\S\S(.*?).html">'
    pat = re.compile(s)
    code = pat.findall(html)
    for item in code:
        if item[0]=='6' or item[0]=='3' or item[0]=='0':
            code_list.append(item)
    return code_list

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

