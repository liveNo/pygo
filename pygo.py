#!/usr/bin/python 
#-*- coding:utf-8

import sys, time, os



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
    login_ln = login_name+'@'+host+' -p '+port
    
    server = pexpect.spawn('/usr/bin/ssh %s' % login_ln)
    server.expect('.*ssword:')
    server.sendline(passwd)
    server.interact()

