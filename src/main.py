#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os, sys, time
from utils import *
import database as db
from request import tencent_request as tquery
import wxpy as wx
import cmd_prompt

top_path = os.path.abspath(os.path.join(sys.path[0], ".."))
cache_path = os.path.join(top_path, "cache")
queue = message_queue.MessageQueue()

class Global:
    timeout_s = 60
    active_chats = {}


def init_wx_app():
    os.chdir(cache_path)
    app = wx.Bot(cache_path= "wxpy.pkl", console_qr=True)
    app.enable_puid(path='wxpy_puid.pkl')

    admin_friend = app.friends(update=True).search('大地小神')[0]
    print("大地小神PUID:%s" % admin_friend.puid)

    eee_stock_group = app.groups(update=True).search('三眼天机')[0]
    print("三眼天机PUID:%s" % eee_stock_group.puid)

    gp_stock_group = app.groups(update=True).search('GP技术流')[0]
    print("GP技术群PUID:%s" % gp_stock_group.puid)

    default_info = dict()
    default_info['until_time'] = -1
    default_info['cmd'] = ''

    Global.active_chats[admin_friend.puid] = default_info
    Global.active_chats[eee_stock_group.puid] = default_info
    Global.active_chats[gp_stock_group.puid] = default_info

    @app.register(chats=[eee_stock_group, gp_stock_group], msg_types=[wx.TEXT], except_self=False)
    def auto_reply_stock_group(msg):
        txt = msg.text.lower()
        chat_info = Global.active_chats[msg.chat.puid]
        if txt == "9":
            chat_info["until_time"] = -1
            if len(chat_info["cmd"]):
                chat_info["cmd"] = ""
                return cmd_prompt.eeequit_str.format(msg.member.name)
            return

        print(chat_info)
        curtime = time.time()
        print(curtime, chat_info["until_time"])
        if curtime < chat_info["until_time"]:
            print("sub menu cmd")
            cmd = chat_info["cmd"]
            if cmd == "eee":
                if txt == "1":
                    chat_info["cmd"] = "eee1"
                    chat_info["until_time"] = curtime + Global.timeout_s
                    return cmd_prompt.system_set_str.format(msg.member.name)
                elif txt == "2":
                    chat_info["cmd"] = "eee2"
                    chat_info["until_time"] = curtime + Global.timeout_s
                    return cmd_prompt.monitor_str.format(msg.member.name)
                elif txt == "3":
                    chat_info["cmd"] = "eee3"
                    chat_info["until_time"] = curtime + Global.timeout_s
                    return cmd_prompt.query_str.format(msg.member.name)
            elif cmd == "eee1":
                if txt == "1" or txt == "2":
                    sql = "select code, name from profile where code='{}' or name like '%%{}%%'"
                    skdb = db.connect_db()
                    cursor = skdb.cursor()
                    try:
                        cursor.execute(sql.format(txt, txt))
                        result = cursor.fetchone()
                        if result == None:
                            return


                    except:
                        return cmd_prompt.inner_error_str.format(msg.member.name)
                    finally:
                        skdb.close()
                return cmd_prompt.notimpl_str.format(msg.member.name)
            elif cmd == "eee2":
                return cmd_prompt.notimpl_str.format(msg.member.name)
            elif cmd == "eee3":
                if txt == "1" or txt == "2" or txt == "3" or txt == "4":
                    chat_info["cmd"] = "eee3" + txt
                    chat_info["until_time"] = curtime + Global.timeout_s
                    return cmd_prompt.input_code_or_name.format(msg.member.name)
            elif cmd == "eee31" or cmd == "eee32" or cmd == "eee33" or cmd == "eee34":
                sql = "select code, name from profile where code='{}' or name like '%%{}%%'"
                skdb = db.connect_db()
                cursor = skdb.cursor()
                try:
                    cursor.execute(sql.format(txt, txt))
                    result = cursor.fetchone()
                    if result == None:
                        return
                    chat_info["until_time"] = curtime + Global.timeout_s
                    if cmd[3] == '1':
                        return cmd_prompt.stock_info_str.format(msg.member.name,
                                tquery.request_brief_info(result[0]))
                    elif cmd[3] == '2':
                        return cmd_prompt.stock_info_str.format(msg.member.name,
                                 tquery.request_latest_quotation(result[0]))
                    elif cmd[3] == '3':
                        return cmd_prompt.stock_info_str.format(msg.member.name,
                                 tquery.request_money_flow(result[0]))
                    elif cmd[3] == '4':
                        return cmd_prompt.stock_info_str.format(msg.member.name,
                                 tquery.request_dish_mouth(result[0]))
                except:
                    return cmd_prompt.inner_error_str.format(msg.member.name)
                finally:
                    skdb.close()
        else:
            # top menu
            if txt == "eee" or txt == "333" or txt == "三眼天机":
                chat_info["cmd"] = "eee"
                chat_info["until_time"] = curtime + Global.timeout_s
                return cmd_prompt.welcome_str.format(msg.member.name)

    @app.register(chats=[admin_friend], msg_types=[wx.TEXT], except_self=False)
    def auto_reply_admin_friend(msg):
        txt = msg.text.lower()
        pass

    return app


def dispatch_message(app, queue):
    while True:
        msg = queue.next()
        msg.handler.handle_message(msg)

if __name__ == "__main__":
    print("current dir: %s, file path: %s" % (os.getcwd(), os.path.split(os.path.realpath(__file__))[0]))
    app = init_wx_app()
    dispatch_message(app, queue)
    #  wx.embed()
