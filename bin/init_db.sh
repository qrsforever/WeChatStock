#!/bin/bash

script_dir=`dirname ${BASH_SOURCE[0]}`

mysqladmin -uroot -p123456 create stock 2>/dev/null

mysql -uroot -p123456 stock <  $script_dir/../conf/stock_db.sql

rm $script_dir/../cache -rf

mkdir -p $script_dir/../cache 
