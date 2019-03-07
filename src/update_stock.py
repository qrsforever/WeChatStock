#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os, time
import database as db
from request import tencent_request as tquery

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

    # Get stock list
    stock_list = tquery.request_stock_list()
    length = len(stock_list)
    print("from {} to {} stock count: {} vs {}".format(start, end, count, length))
    if count != length:
        skdb = db.connect_db()
        cursor = skdb.cursor()
        sql = "replace into profile(code, name) values ('{}', '{}')"
        for (name, code) in stock_list:
            try:
                cursor.execute(sql.format(code, name))
            except Exception as e:
                print("error:", e)
                skdb.rollback()
        skdb.commit()
        skdb.close()

        cf.set(STOCK_COMM_FIELD, "stock_count", str(length))
        cf.write(open(file, "w"))

def query_all_stock():
    skdb = db.connect_db()
    cursor = skdb.cursor()
    sql = "select code, name from profile where code='{}' or name like '%%{}%%'"
    try:
        cursor.execute(sql.format('贵州茅台', '贵州茅台'))
        results = cursor.fetchall()
        for row in results:
            print(row[0], row[1])
    except Exception as e:
        print("error:", e)
    skdb.close()

def update_latest_quotation():
    skdb = db.connect_db()
    cursor = skdb.cursor()
    sql = "select code from profile"

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print("row[0]:", row[0])
            print(tquery.request_latest_quotation(row[0]))
            break

    except Exception as e:
        print("error:", e)
    skdb.close()


if __name__ == "__main__":
    try:
        # update_stock_history()
        # query_all_stock()
        update_latest_quotation()
    except Exception as e:
        print("Exception:", e)
