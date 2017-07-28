# -*- coding:utf8 -*-
import time
from threading import Timer
import Devices


class TimeAction():
    def __init__(self,driver):
        self.driver=driver

    def tap_screen(self):
        self.driver.tap([(992, 614)])
        print "点击屏幕，不要锁屏啦"




