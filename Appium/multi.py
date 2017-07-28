# #-*- coding:utf8 -*-
import unittest
import time
from appium import webdriver
import os
import HtmlTestRunner
import desire_caps
from parameterized import parameterized
# # Returns abs path relative to this file and not cwd
# print desire_caps.Desired_Caps_HuaWei_P9
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
def Desired_Caps_HuaWei_P9():
    desired_caps_HuaWei_P9 = {}
    desired_caps_HuaWei_P9['platformName'] = 'Android'
    desired_caps_HuaWei_P9['platformVersion'] = '7.0'
    desired_caps_HuaWei_P9['deviceName'] = 'generic_a15'
    desired_caps_HuaWei_P9['app'] = PATH('/Users/wangyu/Downloads/taptap_beta_1.8.7_20170522_10_28.apk')
    desired_caps_HuaWei_P9['app-package'] = 'com.taptap'
    desired_caps_HuaWei_P9['app-activity'] = 'com.play.taptap.ui.MainAct'
    HuaWei_P9=webdriver.Remote('http://localhost:4723/wd/hub', desired_caps_HuaWei_P9)


def Desired_Caps_HuaWei_H8():
    desired_caps_HuaWei_H8 = {}
    desired_caps_HuaWei_H8['platformName'] = 'Android'
    desired_caps_HuaWei_H8['platformVersion'] = '7.0'
    desired_caps_HuaWei_H8['deviceName'] = 'generic_a15'
    desired_caps_HuaWei_H8['app'] = PATH('/Users/wangyu/Downloads/taptap_beta_1.8.7_20170522_10_28.apk')
    desired_caps_HuaWei_H8['app-package'] = 'com.taptap'
    desired_caps_HuaWei_H8['app-activity'] = 'com.play.taptap.ui.MainAct'
    desired_caps_HuaWei_H8['udid'] = 'GSL7N16B18008245'
    HuaWei_H8 = webdriver.Remote('http://localhost:4725/wd/hub', desired_caps_HuaWei_H8)



