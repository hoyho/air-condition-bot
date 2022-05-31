# -*- encoding=utf8 -*-
__author__ = "hoyho"

from airtest.core.api import *




dev = device()  # 获取当前手机设备
# 手指按照顺序依次滑过个坐标
dev.swipe_along([[844, 1396],[546, 1387],[238, 1076],[549, 1089],[850, 1089]])

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
poco("com.tencent.mm:id/qi").click()
poco("com.tencent.mm:id/li").click()
poco("com.tencent.mm:id/li").set_text("gzhu")
poco("com.tencent.mm:id/c2c").click()

auto_setup(__file__)
