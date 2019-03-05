#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os, time
import database as db
import download as dd

from configparser import ConfigParser

TOP_DIR = "../"

STOCK_COMM_FIELD = "common"

def update_stock_history():
    file = os.path.join(TOP_DIR, "cache", "stock_history_rec.txt")
    cf = ConfigParser()
    if not os.path.exists(file):
        cf.add_section(STOCK_COMM_FIELD)
        cf.set(STOCK_COMM_FIELD, "lastest_date", "20190201")
        cf.set(STOCK_COMM_FIELD, "stock_count", "0")
        cf.write(open(file, "w"))

    cf.read(file)
    start = cf.get(STOCK_COMM_FIELD, "lastest_date")
    end = time.strftime('%Y%m%d', time.localtime(time.time()-86400))
    if start == end:
        return

    count = cf.getint(STOCK_COMM_FIELD, "stock_count")

    # Get stock codes
    codes = dd.request_stock_codes()
    length = len(codes)
    print("from {} to {} stock count: {} vs {}".format(start, end, count, length))
    if count != length:
        cf.set(STOCK_COMM_FIELD, "stock_count", str(length))
        cf.write(open(file, "w"))

    for data in dd.request_stock_data(codes, start, end):
        print(data)


if __name__ == "__main__":
    try:
        update_stock_history()
    except Exception as e:
        print("Exception:", e)
