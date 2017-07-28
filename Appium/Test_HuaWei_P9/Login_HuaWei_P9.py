#-*- coding:utf8 -*-
import unittest
import time
from appium import webdriver
import os
import HtmlTestRunner
import appium
from Parametrized.ParametrizedTestCase import ParametrizedTestCaseDevice
import Devices

class Test_LoginTestCase(ParametrizedTestCaseDevice):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        print 'reset app'
        Devices.HuaWei_P9.driver.reset()

    def setUp(self):
        self.TestData={}
        self.TestData={'username':'wy006@163.com','pwd':'zty7211'}

    def tearDown(self):
        self.TestData={}
        self.param.reset()
#login_testcase_01:邮箱登录
    try:
        def test_01_Login_TapTap(self):
            time.sleep(5)
            self.param.find_element_by_id('com.taptap:id/head_portrait').click()
            time.sleep(3)
            self.param.find_element_by_id('com.taptap:id/switch_mode').click()
            time.sleep(2)
            self.param.find_element_by_id('com.taptap:id/mail').click()
            time.sleep(3)
            self.param.find_element_by_id('com.taptap:id/login_username').send_keys('wy006@163.com11')
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
            self.assertEqual(TaperID_Tapaccount, 'ID:254776')
            time.sleep(3)

    except Exception as e:
        print e

# login_testcase_02:第三方登录:微信
    try:
        def test_02_Login_WeChat(self):
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
            self.param.find_element_by_id('com.taptap:id/webchat').click()
            time.sleep(5)
            self.param.tap([(100, 1200)])
            time.sleep(5)
            Taper_WeChat = self.param.find_element_by_xpath("//android.widget.TextView[@text='066@Mobile , ID:7034234']")
            Taper_WeChat_text = Taper_WeChat.text
            Taper_ID_Wechat = str(Taper_WeChat_text[13:])
            self.assertEqual(Taper_ID_Wechat, 'ID:7034234')
            time.sleep(3)
            print 'WeChat Login Sucessfully!'
    except Exception as e:
        print e


# login_testcase_03:第三方登录：QQ
    try:
        def test_03_Login_QQ(self):
            time.sleep(3)
            self.param.find_element_by_id('com.taptap:id/setting_account').click()
            time.sleep(3)
            self.param.find_element_by_id('com.taptap:id/relogin').click()
            time.sleep(3)
            self.param.find_element_by_id('com.taptap:id/qq').click()
            time.sleep(3)
            self.param.tap([(578, 1484)])
            time.sleep(3)
            self.param.find_element_by_xpath("//android.widget.ImageButton[@index=0]").click()
            time.sleep(2)
            self.param.find_element_by_xpath("//android.widget.ImageButton[@index='0']").click()
            time.sleep(2)
            self.param.find_element_by_xpath(
                    "//android.widget.FrameLayout[contains(@resource-id,'com.taptap:id/head_portrait')]").click()
            Taper_QQ_ID = self.param.find_element_by_id('com.taptap:id/taper_id').text
            self.assertEqual(Taper_QQ_ID, 'ID:7014430')
            time.sleep(3)
    except Exception as e:
            print e


