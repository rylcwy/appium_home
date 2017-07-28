#-*- coding:utf8 -*-
# Returns abs path rdriverative to this file and not cwd
import os
import time
from appium import webdriver
import os
import unittest
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'generic_a15'
desired_caps['app'] = PATH('/Users/wangyu/Downloads/taptap_waice_1.8.9.1_20170622_10_21.apk')
desired_caps['app-package'] = 'com.taptap'
desired_caps['app-activity'] = 'com.play.taptap.ui.MainAct'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(5)
driver.find_element_by_id('com.taptap:id/head_portrait').click()
time.sleep(3)
driver.find_element_by_id('com.taptap:id/login_by_taptap').click()
time.sleep(3)
driver.find_element_by_id('com.taptap:id/login_username').send_keys('wy006@163.com')
time.sleep(3)
driver.find_element_by_id('com.taptap:id/login_pwd').send_keys('zty7211')
time.sleep(3)
driver.find_element_by_id('com.taptap:id/login').click()
time.sleep(3)
driver.reset()