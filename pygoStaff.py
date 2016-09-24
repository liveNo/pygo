#!/usr/bin/python
#-*- coding=utf-8 -*-

class Pygo (object):
    """
    对像化Pygo
    """
    def __init__ (object):
        pass

    def showHeadTip (object):
        start_line  = '###################################\r\n'
        tip_line    = '##       Python SSH Login\r\n'
        end_line    = '###################################\r\n\r\n'

        # bannar_line =  '选择器|       主机    |  端口 | 登录用户 |  说明\r\n'

        first_option = '选择器'
        second_option = '主机'
        third_option = '端口'
        fourth_option = '登录用户'
        fifth_option = '说明'

        bannar_line = "%s|%s|%s|%s|%s" % (first_option.center(20), second_option.center(20), third_option.center(20), fourth_option.center(20), fifth_option.center(20)) 

        return start_line+tip_line+end_line+bannar_line


    def showHostList (object):
        pass


pygo = Pygo()

print pygo.showHeadTip();
