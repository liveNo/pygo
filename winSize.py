#!/usr/bin/python
# -*- coding=utf-8 -*-
# 获取当前窗口size 

import sys
import time
import pexpect
import os
import struct
import fcntl
import termios
import signal

def getwinsize():
    if 'TIOCGWINSZ' in dir(termios):
        TIOCGWINSZ = termios.TIOCGWINSZ
    else:
        TIOCGWINSZ = 1074295912L # Assume
    
    s = struct.pack('HHHH', 0, 0, 0, 0)
    x = fcntl.ioctl(sys.stdout.fileno(), TIOCGWINSZ, s)
    return struct.unpack('HHHH', x)[0:2]



print getwinsize()
