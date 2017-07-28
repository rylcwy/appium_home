#-*- coding:utf8 -*-
import time
from appium import webdriver
import os
import HtmlTestRunner
import unittest
from nose_parameterized import parameterized
import multi
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
__metaclass__ = type
multi.Desired_Caps_HuaWei_P9()
class LoginTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print 'class setup'
        print 'caps_huawei_p9'
        print 'caps_huawei_H8'

    @classmethod
    def tearDownClass(cls):
        print 'class teardown'
        cls.driver.reset()


    def setUp(self):
        #print 'fouction setup'
        self.TestData={}
        self.TestData={'username':'wy006@163.com','pwd':'zty7211'}

    def tearDown(self):
        print 'fouction teardown'
        #self.driver.close_app()

#login_testcase_01:正常登录
    @parameterized.expand([("P9", multi.Desired_Caps_HuaWei_P9()),("H8",multi.Desired_Caps_HuaWei_H8())])

    def Test_Login_TapTap_P9_01(self,name,device):
        time.sleep(5)
        self.device.find_element_by_id('com.taptap:id/head_portrait').click()
        self.device.find_element_by_id('com.taptap:id/head_portrait').click()
        time.sleep(3)
        self.device.find_element_by_id('com.taptap:id/login_by_taptap').click()
        time.sleep(3)
        self.device.find_element_by_id('com.taptap:id/login_username').send_keys(self.TestData['username'])
        time.sleep(3)
        self.device.find_element_by_id('com.taptap:id/login_pwd').send_keys(self.TestData['pwd'])
        time.sleep(3)
        self.device.find_element_by_id('com.taptap:id/login').click()
        time.sleep(3)
        self.device.find_element_by_id('com.taptap:id/dialog_btn_left').click()
        time.sleep(2)
        self.device.swipe(75, 500, 75, 0, 800)
        self.device.find_element_by_xpath(
            "//android.widget.FrameLayout[contains(@resource-id,'com.taptap:id/head_portrait')]").click()
        TaperID_Tapaccount = self.device.find_element_by_id('com.taptap:id/taper_id').text
        self.assertEqual(TaperID_Tapaccount,'ID:254776')
        time.sleep(3)
        print 'TapTap Account Login Sucessfully!'




if __name__ == "__main__":
    suite=unittest.TestSuite()
    suite.addTest(LoginTestCase("Test_Login_TapTap_P9_01"))
    filename='/Users/wangyu/PycharmProjects/TestReport'
    runner=HtmlTestRunner.HTMLTestRunner(output=filename,report_title='Login_Test_result')
    runner.run(suite)