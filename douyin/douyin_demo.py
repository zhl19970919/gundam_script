import time
import uiautomator2 as u2


def gundam_script():
    d = u2.connect()
    d.press("home")
    d.app_start('com.zhiliaoapp.musically')
    d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/exl"]/android.widget.ImageView[2]').click()
    d.set_fastinput_ime(True)  #
    d.send_keys("")  # adb广播输入
    d.set_fastinput_ime(False)  # 切换成正常的输入法
    d.send_action("search")
    time.sleep(5)
    d.app_stop('com.zhiliaoapp.musically')