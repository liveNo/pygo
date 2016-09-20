#!/usr/bin/python 
#-*- coding:utf-8

import sys, time, os, struct, fcntl, termios, signal




def getwinsize():
    if 'TIOCGWINSZ' in dir(termios):
        TIOCGWINSZ = termios.TIOCGWINSZ
    else:
        TIOCGWINSZ = 1074295912L # Assume
    
    s = struct.pack('HHHH', 0, 0, 0, 0)
    x = fcntl.ioctl(sys.stdout.fileno(), TIOCGWINSZ, s)
    return struct.unpack('HHHH', x)[0:2]



def login (addr):

    try:
        import pexpect
    except ImportError:
        print """
        使用pygo，必须安装pexpect模块
        """
        sys.exit(1)
    try:
        host        = str(addr['host'])
        port        = str(addr['port'])
        login_name  = str(addr['login_name'])
        passwd      = str(addr['password'])
    except:
        print """
        请在config_db_default中完善ssh登录信息
        """
        sys.exit(1)

    winsize = getwinsize();
    login_ln = login_name+'@'+host+' -p '+port
    
    server = pexpect.spawn('/usr/bin/ssh %s' % login_ln)
    server.expect('.*ssword:')
    server.sendline(passwd)
    server.setwinsize(winsize[0], winsize[1])
    server.interact()

