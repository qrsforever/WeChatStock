#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

def admin_friend_reply(top_path, txt):
    if txt == "help":
        print("[1] upgrade: git pull project")
    elif txt == "upgrade" or "1" == txt[0]:
        os.system('git pull %s >/dev/null 2>&1' % top_path)
        print("upgrade ok")
    else:
        print("not support command")


if __name__ == "__main__":
    admin_friend_reply(sys.argv[1], sys.argv[2])
