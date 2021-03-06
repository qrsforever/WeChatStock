# WeChatStock

WeChatStock: talk about stock with wechat


# Required Dependences

- `sudo pip install -U wxpy` [-i "https://pypi.doubanio.com/simple/"]

- `sudo pip install -U pillow` 终端显示二维码

- `sudo apt-get install okular` 看epub文档

- `sudo apt-get install mysql-server mysql-client`

- `sudo pip3 install PyMySQL`

# 字符对应关系

英文|中文
:----:|:--:
TCLOSE    |  收盘价
HIGH      |  最高价
LOW       |  最低价
TOPEN     |  开盘价
LCLOSE    |  前收盘
CHG       |  涨跌额
PCHG      |  涨跌幅
TURNOVER  |  换手率
VOTURNOVER|  成交量
VATURNOVER|  成交金额
TCAP      |  总市值
MCAP      |  流通市值

# 腾讯API

## 最新行情

`http://qt.gtimg.cn/q=sh600519`

```
 0: 未知
 1: 股票名字
 2: 股票代码
 3: 当前价格
 4: 昨收
 5: 今开
 6: 成交量（手）
 7: 外盘
 8: 内盘
 9: 买一
10: 买一量（手）
11-18: 买二 买五
19: 卖一
20: 卖一量
21-28: 卖二 卖五
29: 最近逐笔成交
30: 时间
31: 涨跌
32: 涨跌%
33: 最高
34: 最低
35: 价格/成交量（手）/成交额
36: 成交量（手）
37: 成交额（万）
38: 换手率
39: 市盈率
40: 
41: 最高
42: 最低
43: 振幅
44: 流通市值
45: 总市值
46: 市净率
47: 涨停价
48: 跌停价
```

## 实时资金流向

`http://qt.gtimg.cn/q=ff_sh600519`

```
 0: 股票代码
 1: 主力流入
 2: 主力流出
 3: 主力净流入
 4: 主力净流入/资金流入流出总和
 5: 散户流入
 6: 散户流出
 7: 散户净流入
 8: 散户净流入/资金流入流出总和
 9: 资金流入流出总和1+2+5+6
10: 未知
11: 未知
12: 名字
13: 日期
```

## 获取盘口分析

`http://qt.gtimg.cn/q=s_pksh600519`

```
0: 买盘大单
1: 买盘小单
2: 卖盘大单
3: 卖盘小单
```

## 简要信息

`http://qt.gtimg.cn/q=s_sh600519`

```
 0: 未知
 1: 股票名称
 2: 股票代码
 3: 当前价格
 4: 涨跌
 5: 涨跌%
 6: 成交量（手）
 7: 成交额（万）
 8: 
 9: 总市值
```

# Others

- [wxpy](https://wxpy.readthedocs.io/zh/latest/index.html)

- [腾迅股票数据接口](http://www.cnblogs.com/skating/p/6424342.html)

- [PyMySQL 学习](http://www.runoob.com/python3/python3-mysql.html)
