#-*- coding:utf8 -*-
from appium import webdriver
import time
import os
import sys

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class devices():
    """
    定义devices类
    """
    def __init__(self,host,port,platformName,platformVersion,deviceName,app,app_package,app_activity,udid,newCommandTimeout):
        self.desired_caps = {}
        self.desired_caps['platformName']=platformName
        self.desired_caps['platformVersion']=platformVersion
        self.desired_caps['deviceName']=deviceName
        self.desired_caps['app']=app
        self.desired_caps['app_package']=app_package
        self.desired_caps['app_activity']=app_activity
        self.desired_caps['udid']=udid
        self.desired_caps['newCommandTimeout']=newCommandTimeout
        url="http://"+host+":"+str(port)+"/wd/hub"
        self.driver=webdriver.Remote(url,self.desired_caps)
        time.sleep(5)



#华为P9
#HuaWei_P9=devices('localhost','4725','Android','7.0','generic_a15',PATH('/Users/wangyu/Downloads/taptap_waice_1.9.1.1_add_shell.apk'),'com.taptap','com.play.taptap.ui.MainAct','KWG7N16727001846','20')
#print "实例化华为"
#锤子
#ChuiZi=devices('localhost','4723','Android','7.1','Rock',PATH('/Users/wangyu/Downloads/taptap_waice_1.9.1.1_add_shell.apk'),'com.taptap','com.play.taptap.ui.MainAct','35c5c245','20')
#print "实例化锤子"