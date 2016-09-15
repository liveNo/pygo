#!/usr/bin/python
#-*- coding=utf-8 -*-
import config_db_default
import pygo
configs =  config_db_default.configs



def initHead ():
    print '###################################'
    print '##       Python SSH Login'
    print '###################################'
    print '\r\n'


def initTitle ():
    print '选择器|       主机    |  端口 | 登录用户 |  说明'



def initList (configs):
    for item in configs:
        print '-' * 70;
        print item, ' |', configs[item]['host'], '| ', configs[item]['port'], '|', configs[item]['login_name'], '     |', configs[item]['introduce']

def initFooter ():
    print '-' * 70;
    selector = raw_input('[*] 选择主机:');
    return selector


initHead()
initTitle()
initList(configs)
selector = initFooter();


if (selector == 'q' or selector == 'Q'):
    exit()
else:
    if (configs.has_key(selector)): 
        # print configs[selector]
        pygo.login(configs[selector])
        # print 'HAHA! 欢迎登录', selector
    else: 
        initHead()
        initTitle()
        initList(configs)
        selector = initFooter();
    


