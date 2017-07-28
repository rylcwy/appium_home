 #-*- coding:utf8 -*-
import unittest

from Devices import devices
from Parametrized.ParametrizedTestCase import ParametrizedTestCaseDevice
from Game_Time import Test_Game_Time
import os

# # Returns abs path relative to this file and not cwd

# desire_caps.Desired_Caps_HuaWei_P9

#实例化Devices
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)



# construct suite and run
ChuiZi=devices('localhost','4723','Android','7.1','Rock',PATH('/Users/wangyu/Downloads/taptap_waice_1.9.1.1_add_shell.apk'),'com.taptap','com.play.taptap.ui.MainAct','35c5c245','20')

filename = '/Users/wangyu/PycharmProjects/TestReport'
#suite赋值
suite_gametime=unittest.TestSuite()


#测试游戏时间
suite_gametime.addTest(ParametrizedTestCaseDevice.parametrize(Test_Game_Time,param=ChuiZi.driver))
#需要运行的suites
allsuites=[suite_gametime]

for suite in allsuites:
    #runner = HtmlTestRunner.HTMLTestRunner(output=filename, report_title='Test_Report')
    runner=unittest.TextTestRunner()
    runner.run(suite)





