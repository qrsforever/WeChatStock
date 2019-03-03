#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os, sys, time
import subprocess
import urllib.request

import wxpy as wx

# 最新行情
query_latest = "http://qt.gtimg.cn/q="

# 实时资金流向
query_money_flow = "http://qt.gtimg.cn/q=ff_"

# 盘口分析
query_dish = "http://qt.gtimg.cn/q=s_pk"

watch_stocks = {}
watch_stocks_last = {}

sleep_time = 5

def main():
    print("current work dir path: %s" % os.getcwd())
    print("file path: %s" % os.path.split(os.path.realpath(__file__))[0])
    print("script file path: %s" % sys.path[0])
    top_path = os.path.abspath(os.path.join(sys.path[0], ".."))
    cache_path = os.path.join(top_path, "cache")
    os.chdir(cache_path)
    print("current work dir path: %s" % os.getcwd())
    bot = wx.Bot(cache_path= "wxpy.pkl", console_qr=True)
    bot.enable_puid(path='wxpy_puid.pkl')

    admin_friend_cmd = os.path.join(top_path, "src", "reply", "admin_friend.py")
    stock_group_cmd = os.path.join(top_path, "src", "reply", "stock_group.py")

    admin_friend = bot.friends(update=True).search('大地小神')[0]
    print("大地小神PUID:%s" % admin_friend)

    stock_group = bot.groups(update=True).search('三眼天机')[0]
    print("三眼天机PUID:%s" % stock_group.puid)

    @bot.register(chats=[stock_group], msg_types=[wx.TEXT], except_self=False)
    def auto_reply_stock_group(msg):
        global watch_stocks
        global watch_stocks_last
        txt = msg.text.lower()
        if txt[0] == "+":
            #  if watch_stocks.has_key(txt[1:]):
                #  return
            watch_stocks[txt[1:]] = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
            watch_stocks_last[txt[1:]] = -2
            return
        elif txt[0] == "-":
            #  if watch_stocks.has_key(txt[1:]):
            del watch_stocks[txt[1:]]
            return
        elif txt == "lw":
            res = []
            for stock in watch_stocks:
                res.append(stock)
            return "list watch: {}".format(",".join(res))

        cmd = '{} {} {}'.format(stock_group_cmd, top_path, txt)
        call = subprocess.Popen(args=cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
        (stdout_data, stderr_data) = call.communicate()
        print(stdout_data, stderr_data)
        return stdout_data.decode("gbk")

    @bot.register(chats=[admin_friend], msg_types=[wx.TEXT], except_self=False)
    def auto_reply_admin_friend(msg):
        global sleep_time
        txt = msg.text.lower()
        if txt[0] == "s":
            sleep_time = int(txt[1:])
        #  if not msg.is_at:
            #  return;
        cmd = '{} {} {}'.format(admin_friend_cmd, top_path, txt)
        call = subprocess.Popen(args=cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
        (stdout_data, stderr_data) = call.communicate()
        print(stdout_data, stderr_data)
        return stdout_data.decode("gbk")

    while True:
        hour = int(time.strftime('%d', time.localtime(time.time())))
        if hour < 9 or hour > 15:
            time.sleep(10)
            continue
        try:
            for stock in watch_stocks:
                ff_url = "{}{}".format(query_money_flow, stock)
                with urllib.request.urlopen(ff_url) as response:
                    html = response.read().decode('utf-8', errors='ignore')
                    html = html[15:-1];
                    data = html.split('~')
                    all_flow = round(float(data[9])/10000)
                    main_inflow = round(float(data[1]))
                    main_inflow_per = round(100 * main_inflow / all_flow)
                    main_outflow = round(float(data[2]))
                    main_outflow_per = round(100 * main_outflow / all_flow)
                    diff = main_inflow_per - main_outflow_per
                    print("%d %d %d %d %d" % (main_inflow , main_outflow, main_inflow_per, main_outflow_per, all_flow))
                    if (watch_stocks_last[stock] != diff and diff >= 3):
                        stock_group.send_msg("%s:[%d %d %d %d %d]" % 
                                (stock, main_inflow , main_outflow, main_inflow_per, main_outflow_per, all_flow))
                        watch_stocks_last[stock] = diff
                    watch_stocks[stock][1] = float(data[1])
                    watch_stocks[stock][9] = float(data[9])
        except:
            print("Err")
        time.sleep(sleep_time)
    #  wx.embed()


if __name__ == "__main__":
    main()
