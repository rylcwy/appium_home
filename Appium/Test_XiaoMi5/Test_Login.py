#-*- coding:utf8 -*-
import unittest
import time
from appium import webdriver
import os
import HtmlTestRunner
import appium
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class LoginTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print 'class setup'
        print 'caps_Xiaomi5'
        Xiaomi5 = {}
        Xiaomi5['platformName'] = 'Android'
        Xiaomi5['platformVersion'] = '6.0'
        Xiaomi5['deviceName'] = 'gemini'
        Xiaomi5['app'] = PATH('/Users/wangyu/Downloads/taptap_waice_1.8.9.1_20170616_10_12.apk')
        Xiaomi5['app-package'] = 'com.taptap'
        Xiaomi5['app-activity'] = 'com.play.taptap.ui.MainAct'
        Xiaomi5['udid'] = '4ca68217'
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', Xiaomi5)

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
    def Test_Login_TapTap_01(self):
        Xiaomi5=self.driver
        time.sleep(5)
        Xiaomi5.find_element_by_id('com.taptap:id/head_portrait').click()
        time.sleep(3)
        Xiaomi5.find_element_by_id('com.taptap:id/login_by_taptap').click()
        time.sleep(3)
        Xiaomi5.find_element_by_id('com.taptap:id/login_username').send_keys(self.TestData['username'])
        time.sleep(3)
        Xiaomi5.find_element_by_id('com.taptap:id/login_pwd').send_keys(self.TestData['pwd'])
        time.sleep(3)
        Xiaomi5.find_element_by_id('com.taptap:id/login').click()
        time.sleep(3)
        Xiaomi5.find_element_by_id('com.taptap:id/dialog_btn_left').click()
        time.sleep(2)
        Xiaomi5.swipe(75, 500, 75, 0, 800)
        Xiaomi5.find_element_by_xpath(
            "//android.widget.FrameLayout[contains(@resource-id,'com.taptap:id/head_portrait')]").click()
        TaperID_Tapaccount = Xiaomi5.find_element_by_id('com.taptap:id/taper_id').text
        self.assertEqual(TaperID_Tapaccount,'ID:254776')
        time.sleep(3)
        print 'TapTap Account Login Sucessfully!'

#login_testcase_02:第三方登录:微信
    @unittest.skip("demonstrating skipping")
    def Test_Login_WeChat_02(self):
        print 'WeChat Login Test Start!'
        Xiaomi5 = self.driver
        time.sleep(3)
        Xiaomi5.find_element_by_xpath("//android.widget.TextView[@text='设置']").click()
        time.sleep(3)
        Xiaomi5.swipe(500,1000,500,300,500)
        time.sleep(3)
        Xiaomi5.find_element_by_xpath("//android.widget.FrameLayout[contains(@resource-id,'com.taptap:id/setting_account')]").click()
        time.sleep(3)
        Xiaomi5.find_element_by_xpath("//android.widget.Button[contains(@resource-id,'com.taptap:id/relogin')]").click()
        time.sleep(3)
        Xiaomi5.find_element_by_xpath("//android.widget.ImageButton[@index=0]").click()
        time.sleep(3)
        Xiaomi5.find_element_by_xpath("//android.widget.ImageButton[@index=0]").click()
        time.sleep(5)
        Xiaomi5.find_element_by_id('com.taptap:id/head_portrait').click()
        time.sleep(3)
        Xiaomi5.find_element_by_id('com.taptap:id/webchat').click()
        time.sleep(8)
        Xiaomi5.tap([(100,1200)])
        time.sleep(5)
        Xiaomi5.find_element_by_xpath(
            "//android.widget.FrameLayout[contains(@resource-id,'com.taptap:id/head_portrait')]").click()
        TaperID_WeCaht = Xiaomi5.find_element_by_id('com.taptap:id/taper_id').text
        self.assertEqual(TaperID_WeCaht, 'ID:4290317')
        time.sleep(3)
        print 'WeChat Login Sucessfully!'

#login_testcase_03:第三方登录：QQ
    def Test_Login_QQ_03(self):
        print 'Login QQ Test Start!'
        Xiaomi5=self.driver
        time.sleep(3)
        Xiaomi5.find_element_by_xpath("//android.widget.TextView[@text='设置']").click()
        time.sleep(3)
        Xiaomi5.swipe(500, 1000, 500, 300, 500)
        time.sleep(3)
        Xiaomi5.find_element_by_xpath(
            "//android.widget.FrameLayout[contains(@resource-id,'com.taptap:id/setting_account')]").click()
        time.sleep(3)
        Xiaomi5.find_element_by_xpath(
            "//android.widget.Button[contains(@resource-id,'com.taptap:id/relogin')]").click()
        time.sleep(3)
        Xiaomi5.find_element_by_xpath("//android.widget.ImageButton[@index=0]").click()
        time.sleep(3)
        Xiaomi5.find_element_by_xpath("//android.widget.ImageButton[@index=0]").click()
        time.sleep(5)
        Xiaomi5.find_element_by_id('com.taptap:id/head_portrait').click()
        time.sleep(3)
        Xiaomi5.find_element_by_id('com.taptap:id/qq').click()
        time.sleep(8)
        Xiaomi5.tap([(400, 1500)])
        time.sleep(5)
        Xiaomi5.find_element_by_xpath(
            "//android.widget.FrameLayout[contains(@resource-id,'com.taptap:id/head_portrait')]").click()
        TaperID_QQ=Xiaomi5.find_element_by_id('com.taptap:id/taper_id').text
        self.assertEqual(TaperID_QQ,'ID:5477750')
        time.sleep(3)
        print 'QQ Login Sucessfully!'



if __name__ == "__main__":
    suite=unittest.TestSuite()
    suite.addTest(LoginTestCase("Test_Login_TapTap_01"))
    suite.addTest(LoginTestCase("Test_Login_WeChat_02"))
    suite.addTest(LoginTestCase("Test_Login_QQ_03"))
    filename='/Users/wangyu/PycharmProjects/TestReport'
    runner=HtmlTestRunner.HTMLTestRunner(output=filename,report_title='Login_Test_result')
    runner.run(suite)