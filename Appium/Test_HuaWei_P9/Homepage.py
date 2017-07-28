#-*- coding:utf8 -*-
import unittest
import time
from appium import webdriver
import os
import HtmlTestRunner
import appium
import Login_HuaWei_P9
from Parametrized.ParametrizedTestCase import ParametrizedTestCaseDevice
#import Runner_HuaWei_P9
import Devices

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class Test_HomePageTestCase(ParametrizedTestCaseDevice):
    #滑动首页
    def test_01_Scoll(self):
        time.sleep(5)
        app_icon=self.param.find_element_by_id('com.taptap:id/recommend_app_top_icon')
        if app_icon:
            return True
        else:
            return False

