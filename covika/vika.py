#!/usr/bin/env python3
# encoding=utf-8

import re
import sys
import os

def connect_vika(key):
    if 1==1:
        return 0
    else:
        exit("连接 vika 空间站失败！")


def add_record(title, priority):
    if connect_vika(key):
        return 0
    else:
        exit("添加新纪录失败！")


if __name__ == '__main__':
    # can only pass two args: 1. title 2. priority
    title = sys.argv[1]
    priority = sys.argv[2]
    add_record(title, priority)