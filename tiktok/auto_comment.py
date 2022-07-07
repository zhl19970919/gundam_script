import time
import uiautomator2 as u2
from apify_client import ApifyClient


def gundam_script() -> bool:
    d = u2.connect('{equipment}')
    d.press("home")
    d.app_start('com.zhiliaoapp.musically')
    d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/exl"]/android.widget.ImageView[2]').click()
    d.set_fastinput_ime(True)  #
    d.send_keys("")  # adb广播输入
    d.set_fastinput_ime(False)  # 切换成正常的输入法
    d.send_action("search")
    d.app_stop('com.zhiliaoapp.musically')
    return True


if __name__ == '__main__':
    apify_client = ApifyClient(token='token', api_url='localhost:8080')
    apify_client.key_value_store()
    gundam_script()
