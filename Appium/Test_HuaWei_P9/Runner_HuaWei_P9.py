# #-*- coding:utf8 -*-
import unittest

from Devices import devices
from Homepage import Test_HomePageTestCase
from Login_HuaWei_P9 import Test_LoginTestCase
from Parametrized.ParametrizedTestCase import ParametrizedTestCaseDevice
from PersonalInfo import Test_PersonallInfo
from Game_Time import Test_Game_Time
import os
# construct suite and run
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

filename = '/Users/wangyu/PycharmProjects/TestReport'

HuaWei_P9=devices('localhost','4725','Android','7.0','generic_a15',PATH('/Users/wangyu/Downloads/taptap_waice_1.9.1.1_add_shell.apk'),'com.taptap','com.play.taptap.ui.MainAct','KWG7N16727001846','20')
#suite赋值
suite_login = unittest.TestSuite()
suite_homepage = unittest.TestSuite()
suite_personalInfo=unittest.TestSuite()
suite_gametime=unittest.TestSuite()
#测试登陆
#suite_login.addTest(ParametrizedTestCaseDevice.parametrize(Test_LoginTestCase, param=Devices.HuaWei_P9.driver))
#测试首页
#suite_homepage.addTest(ParametrizedTestCaseDevice.parametrize(Test_HomePageTestCase, param=Devices.HuaWei_P9.driver))
#测试个人中心
#suite_personalInfo.addTest(ParametrizedTestCaseDevice.parametrize(Test_PersonallInfo,param=Devices.HuaWei_P9.driver))
#测试游戏时间
suite_gametime.addTest(ParametrizedTestCaseDevice.parametrize(Test_Game_Time,param=HuaWei_P9.driver))

#需要运行的suites
allsuites=[suite_gametime]

for suite in allsuites:
    #runner = HtmlTestRunner.HTMLTestRunner(output=filename, report_title='Test_Report')
    runner=unittest.TextTestRunner()
    runner.run(suite)





