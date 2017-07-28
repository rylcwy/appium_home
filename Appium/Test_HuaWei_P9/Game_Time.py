#-*- coding:utf8 -*-
import unittest
import time
from appium import webdriver
import os
import HtmlTestRunner
import appium
from Parametrized.ParametrizedTestCase import ParametrizedTestCaseDevice
import Devices
import exceptions
import sys

class Test_Game_Time(ParametrizedTestCaseDevice):
    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        print 'reset app'


    def setUp(self):
        self.TestData = {}
        self.TestData = {'usr1':{'username': 'wy005@163.com ', 'pwd': '555555'},'usr2':{'username':'wy002@163.com','pwd':'222222'}}
        print(self.param.current_activity)
    def tearDown(self):
        self.param.reset()
        print "reset TapTap"
    @unittest.skip("skip")
    def test_01_game_time(self):
        try:
            time.sleep(3)
            self.param.find_element_by_id('com.taptap:id/head_portrait').click()
            time.sleep(3)
            self.param.find_element_by_id('com.taptap:id/switch_mode').click()
            time.sleep(2)
            self.param.find_element_by_id('com.taptap:id/mail').click()
            time.sleep(3)
            self.param.find_element_by_id('com.taptap:id/login_username').clear()
            self.param.find_element_by_id('com.taptap:id/login_username').send_keys(self.TestData['usr1']['username'])
            time.sleep(3)
            self.param.find_element_by_id('com.taptap:id/login_pwd').send_keys(self.TestData['usr1']['pwd'])
            time.sleep(3)
            self.param.find_element_by_id('com.taptap:id/login').click()
            time.sleep(3)
            self.param.find_element_by_id('com.taptap:id/dialog_btn_right').click()
            time.sleep(2)
            self.param.tap([(582, 1712)])
            time.sleep(2)
            self.param.tap([(950, 423)])
            time.sleep(2)
            self.param.press_keycode(3)
            time.sleep(3)
            self.param.find_element_by_id('com.taptap:id/my_game').click()
            time.sleep(2)
#运行游戏
            self.param.tap([(952,711)])
            time.sleep(2)
            #time_log=open('/Users/wangyu/PycharmProjects/time_log/time_log','w')
            #sys.stdout=time_log
            print "开始时间："+time.strftime('%m-%d-%H-%M-%S', time.localtime())
            time_control=0
            while time_control<=1:
                time.sleep(40)
                print"tap"
                self.param.tap([(992, 614)])
                time_control=time_control+1
                print time_control
        except Exception as e:
            print e
            print "有异常之后结束时间："+time.strftime('%m-%d-%H-%M-%S', time.localtime())
        else:
            print "正常结束："+time.strftime('%m-%d-%H-%M-%S', time.localtime())


    def test_02_game_time_partition(self):
        #try:
            print "case2"
            time.sleep(3)
            self.param.find_element_by_id('com.taptap:id/head_portrait').click()
            time.sleep(3)
            self.param.find_element_by_id('com.taptap:id/switch_mode').click()
            time.sleep(2)
            self.param.find_element_by_id('com.taptap:id/mail').click()
            time.sleep(3)
            self.param.find_element_by_id('com.taptap:id/login_username').clear()
            self.param.find_element_by_id('com.taptap:id/login_username').set_value(self.TestData['usr2']['username'])
            time.sleep(3)
            self.param.find_element_by_id('com.taptap:id/login_pwd').set_value(self.TestData['usr2']['pwd'])
            time.sleep(3)
            self.param.find_element_by_id('com.taptap:id/login').click()
            time.sleep(3)
            self.param.find_element_by_id('com.taptap:id/dialog_btn_right').click()
            time.sleep(2)
            self.param.tap([(582, 1712)])
            time.sleep(3)
            self.param.tap([(950, 423)])
            time.sleep(3)
            self.param.press_keycode(3)
            time.sleep(2)
            self.param.start_activity('com.taptap','com.play.taptap.ui.MainAct')
            time.sleep(3)
            self.param.find_element_by_id('com.taptap:id/my_game').click()
            time.sleep(2)
            # 运行游戏
            self.param.tap([(952, 711)])
            time.sleep(8)
            print "开始时间：" + time.strftime('%m-%d-%H-%M-%S', time.localtime())
            time_control_partition = 0
            while time_control_partition < 30:
                self.param.press_keycode(3)
                print "按home键"
                time.sleep(60)
                self.param.start_activity('com.kumagames.highschoolsimulator2018', 'com.unity3d.player.UnityPlayerActivity')
                time.sleep(60)
                print "打开游戏"
                time_control_partition=time_control_partition+1
        # except Exception as e:
        #     print e
        #     print "发生异常，程序结束" + time.strftime('%m-%d-%H-%M-%S', time.localtime())
        # else:
        #     print "程序正常结束，无异常" + time.strftime('%m-%d-%H-%M-%S', time.localtime())

