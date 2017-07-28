#-*- coding:utf8 -*-
import unittest
import time
from appium import webdriver
import os
import HtmlTestRunner
import appium
import sys
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class LoginTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print 'class setup'
        desired_caps_HuaWei_P9 = {}
        desired_caps_HuaWei_P9['platformName'] = 'Android'
        desired_caps_HuaWei_P9['platformVersion'] = '7.0'
        desired_caps_HuaWei_P9['deviceName'] = 'generic_a15'
        desired_caps_HuaWei_P9['app'] = PATH('/Users/wangyu/Downloads/taptap_waice_1.8.9.1_20170703_14_35.apk')
        desired_caps_HuaWei_P9['app-package'] = 'com.taptap'
        desired_caps_HuaWei_P9['app-activity'] = 'com.play.taptap.ui.MainAct'
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps_HuaWei_P9)


    @classmethod
    def tearDownClass(cls):
        print 'class teardown'
        cls.driver.close_app()


    def setUp(self):
        print 'start'
        self.TestData={}
        self.TestData={'username':'wy006@163.com','pwd':'zty7211'}

    def tearDown(self):
        print 'stop'
        #self.driver.close_app()

#login_testcase_01:正常登录
    try:
        def test_01_Login_TapTap(self):
            HuaWei_P9 = self.driver
            time.sleep(5)
            HuaWei_P9.find_element_by_id('com.taptap:id/head_portrait').click()
            time.sleep(3)
            HuaWei_P9.find_element_by_id('com.taptap:id/switch_mode').click()
            time.sleep(2)
            HuaWei_P9.find_element_by_id('com.taptap:id/mail').click()
            time.sleep(3)
            HuaWei_P9.find_element_by_id('com.taptap:id/login_username').send_keys('wy006@163.com11')
            time.sleep(3)
            HuaWei_P9.find_element_by_id('com.taptap:id/login_pwd').send_keys(self.TestData['pwd'])
            time.sleep(3)
            HuaWei_P9.find_element_by_id('com.taptap:id/login').click()
            time.sleep(3)
            HuaWei_P9.find_element_by_id('com.taptap:id/dialog_btn_left').click()
            time.sleep(2)
            HuaWei_P9.swipe(75, 500, 75, 0, 800)
            HuaWei_P9.find_element_by_xpath(
                "//android.widget.FrameLayout[contains(@resource-id,'com.taptap:id/head_portrait')]").click()
            TaperID_Tapaccount = HuaWei_P9.find_element_by_id('com.taptap:id/taper_id').text
            self.assertEqual(TaperID_Tapaccount, 'ID:254776')
            time.sleep(3)
    except Exception as e:
        print e

#login_testcase_02:第三方登录:微信
    def test_02_Login_WeChat(self):
        HuaWei_P9 = self.driver
        time.sleep(3)
        HuaWei_P9.find_element_by_xpath("//android.widget.TextView[@text='设置']").click()
        time.sleep(3)
        HuaWei_P9.swipe(500,1000,500,300,500)
        time.sleep(3)
        HuaWei_P9.find_element_by_xpath("//android.widget.FrameLayout[contains(@resource-id,'com.taptap:id/setting_account')]").click()
        time.sleep(3)
        HuaWei_P9.find_element_by_xpath("//android.widget.Button[contains(@resource-id,'com.taptap:id/relogin')]").click()
        time.sleep(3)
        HuaWei_P9.find_element_by_id('com.taptap:id/webchat').click()
        time.sleep(5)
        HuaWei_P9.tap([(100,1200)])
        time.sleep(5)
        Taper_WeChat = HuaWei_P9.find_element_by_xpath("//android.widget.TextView[@text='066@Mobile , ID:7034234']")
        Taper_WeChat_text=Taper_WeChat.text
        Taper_ID_Wechat=str(Taper_WeChat_text[13:])
        self.assertEqual(Taper_ID_Wechat,'ID:7034234')
        time.sleep(3)
        print 'WeChat Login Sucessfully!'

#login_testcase_03:第三方登录：QQ
    try:
        def test_03_Login_QQ(self):
            HuaWei_P9 = self.driver
            time.sleep(3)
            HuaWei_P9.find_element_by_id('com.taptap:id/setting_account').click()
            time.sleep(3)
            HuaWei_P9.find_element_by_id('com.taptap:id/relogin').click()
            time.sleep(3)
            HuaWei_P9.find_element_by_id('com.taptap:id/qq').click()
            time.sleep(3)
            HuaWei_P9.tap([(578,1484)])
            time.sleep(3)
            HuaWei_P9.find_element_by_xpath("//android.widget.ImageButton[@index=0]").click()
            time.sleep(2)
            HuaWei_P9.find_element_by_xpath("//android.widget.ImageButton[@index='0']").click()
            time.sleep(2)
            HuaWei_P9.find_element_by_xpath("//android.widget.FrameLayout[contains(@resource-id,'com.taptap:id/head_portrait')]").click()
            Taper_QQ_ID=HuaWei_P9.find_element_by_id('com.taptap:id/taper_id').text
            self.assertEqual(Taper_QQ_ID, 'ID:7014430')
            time.sleep(3)
    except Exception as e:
        print e


if __name__ == "__main__":
    suite = unittest.TestSuite()
    testloader=unittest.TestLoader()
    suite.addTests(testloader.loadTestsFromTestCase(LoginTestCase))
    filename = '/Users/wangyu/PycharmProjects/TestReport'
    runner=unittest.TextTestRunner()
    #runner = HtmlTestRunner.HTMLTestRunner(output=filename, report_title='Login_Test_result')
    runner.run(suite)


