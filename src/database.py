#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import pymysql

from configparser import ConfigParser

TOP_DIR = "../"

MYSQL_FIELD = "MySQL"
DBNAME = "stock"

def connect_db():
    cf = ConfigParser()
    cf.read(os.path.join(TOP_DIR, "conf", "global.conf"))
    db = pymysql.connect(
            host=cf.get(MYSQL_FIELD , "host"),
            port=cf.getint(MYSQL_FIELD , "port"),
            user=cf.get(MYSQL_FIELD , "user"),
            password=cf.get(MYSQL_FIELD , "password"),
            db=DBNAME, charset="utf8")
    print("connect db success.")
    return db

if __name__ == "__main__":
    pass
