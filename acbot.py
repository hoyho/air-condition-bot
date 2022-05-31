# -*- encoding=utf8 -*-
__author__ = "hoyho"

from datetime import datetime
from airtest.core.api import *
from airtest.cli.parser import cli_setup

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.cli.parser import cli_setup
from airtest.core.api import connect_device
import schedule

conn = "Android://127.0.0.1:5037/CB512AAPKE"

if not cli_setup():
    auto_setup(__file__, logdir=False, devices=[conn,])


def turn_on_my_air_conditioner(conn="Android://127.0.0.1:5037/CB512AAPKE"):
    print(datetime.now())
    print("turn_on_my_air_conditioner called ")
    # 传入连接串
    dev = connect_device(conn)
    #dev = connect_device("Android://127.0.0.1:5037/CB512AAPKE")

    poco = AndroidUiautomationPoco(dev)

    dev.home()
    sleep(1)
    if dev.is_locked:
        dev.unlock()
        # use guesture
        sleep(1)
        dev.swipe((1000,1000),(200,1000))
        sleep(2)
        # input guesture
        dev.swipe_along([[235, 1384],[539, 1089],[844, 1396],[546, 1387],[238, 1076],[549, 1089],[850, 1089]])
    # swipe to unlock

    print("launch wechat ...")
    app = dev.start_app("com.tencent.mm")
    time.sleep(3)

    print("swipe down to mini app ...")
    swipe((200,300),(200,1100))


    #click stared hualing icon
    #poco("com.tencent.mm:id/dtj").click()
    sleep(1)
    print("waiting  hualing icon ...")
    touch(Template("resource/hualing_icon.png"))
    time.sleep(6)

    print("wait for 搜索新设备 ...")
    search_new_btn = poco(text="搜索新设备")
    poco.wait_for_any(search_new_btn,timeout=60)

    print("enter my device, it may take seconds ...")
    touch(Template("resource/device_and_blt.png"))
    sleep(6)

    print("turning on air conditioner ...")
    turnon_btn = poco(text="打开空调")
    poco.wait_for_all(turnon_btn,timeout=60)
    turnon_btn.click()
    sleep(3)

    more_btn = poco(text="更多功能")
    poco.wait_for_all(more_btn)
    more_btn.click()
    sleep(5)


    eco_btn_txt = poco(text="ECO")
    eco_btn_pic = Template("resource/eco_btn.png")
    poco.wait_for_any([eco_btn_txt,eco_btn_pic])
    if eco_btn_txt.exists():
        eco_btn_txt.click()
    elif eco_btn_pic.exists():
        eco_btn_pic.click()
    sleep(3)

    keyevent("BACK")
    
    sleep(1)
    prevent_btn = Template("resource/prevent_direct.png")
    poco.wait_for_all([prevent_btn])
    prevent_btn.click()
    sleep(1)
    

    dev.home()


def job():
    try:
        turn_on_my_air_conditioner()
    except Exception as e:
        print(e)
        pass

if __name__ == '__main__':
    print("on start ...")
    print("set up cron")
    turn_on_my_air_conditioner()
    schedule.every().day.at("06:00").do(turn_on_my_air_conditioner)
    while True:
        schedule.run_pending()   # all all scheduled jobs
        time.sleep(1)


