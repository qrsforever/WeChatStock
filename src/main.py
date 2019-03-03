#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os, sys

import wxpy as wx

def main():
    print("current work dir path: %s" % os.getcwd())
    print("file path: %s" % os.path.split(os.path.realpath(__file__))[0])
    print("script file path: %s" % sys.path[0])
    top_path = os.path.join(sys.path[0], "..")
    cache_path = os.path.join(top_path, "cache")
    os.chdir(cache_path)
    print("current work dir path: %s" % os.getcwd())
    bot = wx.Bot(cache_path= "wxpy.pkl", console_qr=True)
    bot.enable_puid(path='wxpy_puid.pkl')

    admin_friend_cmd = os.path.join(top_path, "src", "reply", "admin_friend.py");
    stock_group_cmd = os.path.join(top_path, "src", "reply", "stock_group.py");

    admin_friend = bot.friends(update=True).search('大地小神')[0]
    print("大地小神PUID:%s" % admin_friend)

    stock_group = bot.groups(update=True).search('三眼天机')[0]
    print("三眼天机PUID:%s" % stock_group.puid)

    @bot.register(chats=[stock_group], msg_types=[wx.TEXT], except_self=False)
    def auto_reply_stock_group(msg):
        #  msg.sender.send_msg('收到消息: {} ({})'.format(msg.text, msg.type))
        return '@{} 收到消息: {} ({})'.format(msg.member.name, msg.text, msg.type)

    @bot.register(chats=[admin_friend], msg_types=[wx.TEXT], except_self=False)
    def auto_reply_admin_friend(msg):
        if not msg.is_at:
            return;
        return os.system('{} {} {}'.format(admin_friend, top_path, msg.text.lower())); 

    wx.embed()


if __name__ == "__main__":
    main()
