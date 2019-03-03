#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

# 最新行情
query_latest = "http://qt.gtimg.cn/q="

# 实时资金流向
query_money_flow = "http://qt.gtimg.cn/q=ff_"

# 盘口分析
query_dish = "http://qt.gtimg.cn/q=s_pk"

def stock_group_reply(top_path, txt):
    if txt == "help":
        print("[1] Add/Del watch stock (+/-)")
        print("[x] Market index")
    else:
        print("not support command")


if __name__ == "__main__":
    stock_group_reply(sys.argv[1], sys.argv[2])
