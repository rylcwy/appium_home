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
from selenium.common.exceptions import NoSuchElementException



class Test_PersonallInfo(ParametrizedTestCaseDevice):
    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        print 'reset app'
        #Devices.HuaWei_P9.driver.reset()

    def setUp(self):
        self.TestData = {}
        self.TestData = {'username': 'wy005@163.com', 'pwd': '555555'}
    def tearDown(self):
        Devices.HuaWei_P9.driver.close_app()


#个人中心页元素是否显示
    def test_01_infopage(self):
        time.sleep(3)
        self.param.find_element_by_id('com.taptap:id/head_portrait').click()
        time.sleep(3)
        self.param.find_element_by_id('com.taptap:id/switch_mode').click()
        time.sleep(2)
        self.param.find_element_by_id('com.taptap:id/mail').click()
        time.sleep(3)
        self.param.find_element_by_id('com.taptap:id/login_username').clear()
        self.param.find_element_by_id('com.taptap:id/login_username').send_keys('wy005@163.com  ')
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
#修改资料按钮
        self.param.find_element_by_xpath(
            "//android.widget.Button[contains(@resource-id,'com.taptap:id/taper_modify')]")
#名字
        self.param.find_element_by_id("com.taptap:id/taper_name")
#简介
        self.param.find_element_by_id("com.taptap:id/taper_about")

#评价过的游戏列表
        time.sleep(5)
        evalutenumber = self.param.find_element_by_xpath("//android.widget.TextView[@text='评价 (16)']")
        self.param.find_element_by_xpath("//android.widget.TextView[@text='评价了游戏']")
        time.sleep(3)
        print "1"
        var=0
        while var<10:
            self.param.swipe(500, 1600, 500, 900, 500)
            var=var+1
            print var
            try:
                self.param.find_element_by_xpath("//android.widget.TextView[@text='再见吧恶龙']")
                print "开心，终于找到了"
                break
            except NoSuchElementException:
                print "唉呀，没找到这个元素接着找呗"

#玩过的游戏列表
        self.param.find_element_by_xpath("//android.widget.TextView[@text='玩过 (107)']").click()
        time.sleep(3)
        var2=0
        while var2<30:
            self.param.swipe(500, 1600, 500, 900, 500)
            var2=var2+1
            try:
                self.param.find_element_by_xpath("//android.widget.TextView[@text='拼合碎片']")
                print "开心，终于找到了"
                break
            except NoSuchElementException:
                print "唉呀，没找到这个元素接着找呗"
#帖子页标签
        self.param.find_element_by_xpath("//android.widget.TextView[@text='帖子']").click()
        time.sleep(2)
        self.param.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'com.taptap:id/user_name')and @text='wy005']")
        time.sleep(2)
        self.param.find_element_by_xpath("//android.widget.TextView[@text='回帖 (5)']").click()
        time.sleep(2)
        self.param.find_element_by_xpath("//android.widget.TextView[@text='wy005回复了帖子']")
        time.sleep(2)
        self.param.find_element_by_xpath("//android.widget.TextView[@text='收藏 (3)']").click()
        time.sleep(2)
        self.param.find_element_by_xpath("//android.widget.TextView[contains(@resource-id,'com.taptap:id/chosen_theme_item_brief')and @text='TapTap 发现好游戏 iOS版本上架公告 ']")









