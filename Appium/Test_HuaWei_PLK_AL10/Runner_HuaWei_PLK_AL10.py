# #-*- coding:utf8 -*-
import unittest
import time
from appium import webdriver
import os
import HtmlTestRunner
from parameterized import parameterized
from Parametrized.ParametrizedTestCase import ParametrizedTestCaseDevice
from Test_Login_PLK_AL10 import Test_LoginTestCase

# # Returns abs path relative to this file and not cwd


# desire_caps.Desired_Caps_HuaWei_PLK-AL10
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
desired_caps_HuaWei_PLK_AL10 = {}
desired_caps_HuaWei_PLK_AL10['platformName'] = 'Android'
desired_caps_HuaWei_PLK_AL10['platformVersion'] = '6.0'
desired_caps_HuaWei_PLK_AL10['deviceName'] = 'PLK-AL10'
desired_caps_HuaWei_PLK_AL10['app'] = PATH('/Users/wangyu/Downloads/taptap_waice_1.8.9.1_20170616_10_12.apk')
desired_caps_HuaWei_PLK_AL10['app-package'] = 'com.taptap'
desired_caps_HuaWei_PLK_AL10['app-activity'] = 'com.play.taptap.ui.MainAct'
desired_caps_HuaWei_PLK_AL10['udid'] = 'D8YDU16416006502'
PLK_AL10 = webdriver.Remote('http://localhost:4725/wd/hub', desired_caps_HuaWei_PLK_AL10)


# construct suite and run
filename = '/Users/wangyu/PycharmProjects/TestReport'
suite_login = unittest.TestSuite()
suite_homepage = unittest.TestSuite()
suite_login.addTest(ParametrizedTestCaseDevice.parametrize(Test_LoginTestCase, param=PLK_AL10))

allsuites=[suite_login,suite_homepage]
print allsuites
runner = HtmlTestRunner.HTMLTestRunner(output=filename, report_title='Login_Test_result')
for suite in allsuites:
    runner.run(suite)
