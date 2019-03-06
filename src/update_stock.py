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

    # Get stock list
    stock_list = dd.request_stock_list()
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


if __name__ == "__main__":
    try:
        #  update_stock_history()
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
    except Exception as e:
        print("Exception:", e)
