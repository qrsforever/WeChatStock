#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

def admin_friend_reply(top_path, txt):
    print('git pull %s' % top_path)
    if txt == "upgrade":
        os.system('git pull %s' % top_path);

if __name__ == "__main__":
    admin_friend_reply(sys.argv[1], sys.argv[2])
