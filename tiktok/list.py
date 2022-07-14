import time
import uiautomator2 as u2
from apify_client import ApifyClient


def gundam_script() -> bool:
    d = u2.connect('{equipment}')
    d.press("home")
    d.app_start('com.zhiliaoapp.musically')
    d.xpath('//*[@resource-id="com.zhiliaoapp.musically:id/exl"]/android.widget.ImageView[1]').click()
    d.set_fastinput_ime(True)  #
    d.send_keys("cat")  # adb广播输入
    d.set_fastinput_ime(False)  # 切换成正常的输入法
    d.send_action("search")
    d(resourceId="com.zhiliaoapp.musically:id/cry").click()
    d(resourceId="com.zhiliaoapp.musically:id/g1r", text="Yesterday").click()
    d(resourceId="com.zhiliaoapp.musically:id/g1r", text="Most liked").click()
    d(resourceId="com.zhiliaoapp.musically:id/dof").click()
    d.swipe_ext("left")
    d.swipe_ext("left")
    return True

if __name__ == '__main__':
    # apify_client = ApifyClient(token='token', api_url='localhost:8080')
    # apify_client.key_value_store()
    gundam_script()
