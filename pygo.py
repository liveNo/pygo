#!/usr/bin/python 
#-*- coding:utf-8

import sys, time, os

try:
    import pexpect
except ImportError:
    print """
    You must install pexpect module
    """
    sys.exit(1)


if len(sys.argv) > 1 :
    key = sys.argv[1]
else:
    key = 'sporte'


addr_map = {
        '122': ('root@192.168.1.122 -p 9002', '2016!@#apu11fjjli'),
        '123': ('example@192.168.1.123 -p 9002', 'mi&*!#%$$15')
        }
try:
    host = addr_map[key]
except:
    print """
        Please select correct option! 
    """
    sys.exit(1)


server = pexpect.spawn('/usr/bin/ssh %s' % host[0])
server.expect('.*ssword:')
server.sendline(host[1])
server.interact()
