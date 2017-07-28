# #-*- coding:utf8 -*-
import unittest
import time
from appium import webdriver
import os
import HtmlTestRunner
from parameterized import parameterized
import xunitparser
# # Returns abs path relative to this file and not cwd
# print desire_caps.Desired_Caps_HuaWei_P9
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
desired_caps_HuaWei_P9 = {}
desired_caps_HuaWei_P9['platformName'] = 'Android'
desired_caps_HuaWei_P9['platformVersion'] = '7.0'
desired_caps_HuaWei_P9['deviceName'] = 'generic_a15'
desired_caps_HuaWei_P9['app'] = PATH('/Users/wangyu/Downloads/taptap_beta_1.8.7_20170522_10_28.apk')
desired_caps_HuaWei_P9['app-package'] = 'com.taptap'
desired_caps_HuaWei_P9['app-activity'] = 'com.play.taptap.ui.MainAct'
desired_caps_HuaWei_P9['udid']='KWG7N16727001846'
HuaWei_P9=webdriver.Remote('http://localhost:4723/wd/hub', desired_caps_HuaWei_P9)

#
# desired_caps_HuaWei_PLK_AL10 = {}
# desired_caps_HuaWei_PLK_AL10['platformName'] = 'Android'
# desired_caps_HuaWei_PLK_AL10['platformVersion'] = '6.0'
# desired_caps_HuaWei_PLK_AL10['deviceName'] = 'PLK-AL10'
# desired_caps_HuaWei_PLK_AL10['app'] = PATH('/Users/wangyu/Downloads/taptap_beta_1.8.7_20170522_10_28.apk')
# desired_caps_HuaWei_PLK_AL10['app-package'] = 'com.taptap'
# desired_caps_HuaWei_PLK_AL10['app-activity'] = 'com.play.taptap.ui.MainAct'
# desired_caps_HuaWei_PLK_AL10['udid']='D8YDU16416006502'
# HuaWei_PLK_AL10 = webdriver.Remote('http://localhost:4725/wd/hub', desired_caps_HuaWei_PLK_AL10)


class LoginTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print 'class setup'

    @classmethod
    def tearDownClass(cls):
        print 'class teardown'
        cls.driver.close_app()

    def setUp(self):
        #print 'fouction setup'
        self.TestData={}
        self.TestData={'username':'wy006@163.com','pwd':'zty7211'}

    def tearDown(self):
        print 'fouction teardown'
        #self.driver.close_app()

#login_testcase_01:正常登录
    def test_Login_TapTap_P9_01(self):
        time.sleep(5)
        device.find_element_by_id('com.taptap:id/head_portrait').click()
        time.sleep(3)
        device.find_element_by_id('com.taptap:id/login_by_taptap').click()
        time.sleep(3)
        device.find_element_by_id('com.taptap:id/login_username').send_keys(self.TestData['username'])



if __name__ == "__main__":

    suite=unittest.TestSuite()
    suite.addTest(LoginTestCase("test_Login_TapTap_P9_01"))
    filename='/Users/wangyu/PycharmProjects/TestReport'
    runner=HtmlTestRunner.HTMLTestRunner(output=filename,report_title='Login_Test_result')
    runner.run(suite)
