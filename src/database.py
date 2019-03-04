#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import pymysql
from configparser import ConfigParser

FIELD = "MySQL"
DBNAME = "stock"

def connect_db(top_path):
    cf = ConfigParser()
    cf.read(os.path.join(top_path, "conf", "global.conf"))
    print(os.path.join(top_path, "conf", "global.conf"))
    db = pymysql.connect(
            host=cf.get(FIELD , "host"),
            port=cf.getint(FIELD , "port"),
            user=cf.get(FIELD , "user"),
            password=cf.get(FIELD , "password"),
            db=DBNAME, charset="utf8")
    print("connect db success.")
    return db

if __name__ == "__main__":
    try:
        connect_db("../../")
    except Exception as e:
        print("connect db fail", e)
