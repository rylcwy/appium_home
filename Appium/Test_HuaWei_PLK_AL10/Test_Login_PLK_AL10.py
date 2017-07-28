#-*- coding:utf8 -*-
import unittest
import time
from appium import webdriver
import os
import HtmlTestRunner
import appium
from Parametrized.ParametrizedTestCase import ParametrizedTestCaseDevice
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class Test_LoginTestCase(ParametrizedTestCaseDevice):
    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        cls.
    def setUp(self):
        #print 'fouction setup'
        self.TestData={}
        self.TestData={'username':'wy006@163.com','pwd':'zty7211'}

    def tearDown(self):
        print 'fouction teardown'
        self.driver.close_app()

#login_testcase_01:正常登录
    def test_01_Login_TapTap(self):
        time.sleep(5)
        self.param.find_element_by_id('com.taptap:id/head_portrait').click()
        time.sleep(3)
        self.param.find_element_by_id('com.taptap:id/login_by_taptap').click()
        time.sleep(3)
        self.param.find_element_by_id('com.taptap:id/login_username').send_keys(self.TestData['username'])
        time.sleep(3)
        self.param.find_element_by_id('com.taptap:id/login_pwd').send_keys(self.TestData['pwd'])
        time.sleep(3)
        self.param.find_element_by_id('com.taptap:id/login').click()
        time.sleep(3)
        self.param.find_element_by_id('com.taptap:id/dialog_btn_left').click()
        time.sleep(2)
        self.param.swipe(75, 500, 75, 0, 800)
        self.param.find_element_by_xpath(
            "//android.widget.FrameLayout[contains(@resource-id,'com.taptap:id/head_portrait')]").click()
        TaperID_Tapaccount = self.param.find_element_by_id('com.taptap:id/taper_id').text
        self.assertEqual(TaperID_Tapaccount,'ID:254776')
        time.sleep(3)
        print 'TapTap Account Login Sucessfully!'

#login_testcase_02:第三方登录:微信
    def test_02_Login_WeChat(self):
        print 'WeChat Login Test Start!'
        time.sleep(3)
        self.param.find_element_by_xpath("//android.widget.TextView[@text='设置']").click()
        time.sleep(3)
        self.param.swipe(500,1000,500,300,500)
        time.sleep(3)
        self.param.find_element_by_xpath("//android.widget.FrameLayout[contains(@resource-id,'com.taptap:id/setting_account')]").click()
        time.sleep(3)
        self.param.find_element_by_xpath("//android.widget.Button[contains(@resource-id,'com.taptap:id/relogin')]").click()
        time.sleep(3)
        self.param.find_element_by_xpath("//android.widget.ImageButton[@index=0]").click()
        time.sleep(3)
        self.param.find_element_by_xpath("//android.widget.ImageButton[@index=0]").click()
        time.sleep(5)
        self.param.find_element_by_id('com.taptap:id/head_portrait').click()
        time.sleep(3)
        self.param.find_element_by_id('com.taptap:id/webchat').click()
        time.sleep(8)
        self.param.tap([(100,1200)])
        time.sleep(5)
        self.param.find_element_by_xpath(
            "//android.widget.FrameLayout[contains(@resource-id,'com.taptap:id/head_portrait')]").click()
        TaperID_WeCaht = self.param.find_element_by_id('com.taptap:id/taper_id').text
        self.assertEqual(TaperID_WeCaht, 'ID:4290317')
        time.sleep(3)
        print 'WeChat Login Sucessfully!'

#login_testcase_03:第三方登录：QQ
    @unittest.skip("demonstrating skipping")
    def test_03_Login_QQ(self):
        print 'Login QQ Test Start!'
        time.sleep(3)
        self.param.find_element_by_xpath("//android.widget.TextView[@text='设置']").click()
        time.sleep(3)
        self.param.swipe(500, 1000, 500, 300, 500)
        time.sleep(3)
        self.param.find_element_by_xpath(
            "//android.widget.FrameLayout[contains(@resource-id,'com.taptap:id/setting_account')]").click()
        time.sleep(3)
        self.param.find_element_by_xpath(
            "//android.widget.Button[contains(@resource-id,'com.taptap:id/relogin')]").click()
        time.sleep(3)
        self.param.find_element_by_xpath("//android.widget.ImageButton[@index=0]").click()
        time.sleep(3)
        self.param.find_element_by_xpath("//android.widget.ImageButton[@index=0]").click()
        time.sleep(5)
        self.param.find_element_by_id('com.taptap:id/head_portrait').click()
        time.sleep(3)
        self.param.find_element_by_id('com.taptap:id/qq').click()
        time.sleep(8)
        self.param.tap([(400, 1500)])
        time.sleep(5)
        self.param.find_element_by_xpath(
            "//android.widget.FrameLayout[contains(@resource-id,'com.taptap:id/head_portrait')]").click()
        TaperID_QQ=self.param.find_element_by_id('com.taptap:id/taper_id').text
        self.assertEqual(TaperID_QQ,'ID:5477750')
        time.sleep(3)
        print 'QQ Login Sucessfully!'
