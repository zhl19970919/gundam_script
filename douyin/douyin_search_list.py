
import utils.push
import uiautomator2 as u2


# 仅适用于抖音18.5.0其他版本未测试xpath

def gundam_script() -> bool:
    # d = u2.connect('{equipment}')
    try:
        d = u2.connect('$equipment')
        #d = u2.connect("25cb279e")
        d.press("home")
        d.app_stop("com.ss.android.ugc.aweme")
        d.app_start("com.ss.android.ugc.aweme")
        with d.watch_context() as ctx:
            ctx.when("^(DENY|拒绝)").when("(允许|ALLOW)").click()
            ctx.when("同意").click()
            ctx.when("确定").click()
            ctx.wait_stable()
        d(resourceId="com.ss.android.ugc.aweme:id/e5r").click()
        d(focused=True).set_text("$searchWord")
        d.send_action("search")
        d(resourceId="com.ss.android.ugc.aweme:id/de8").click()
        d(resourceId="com.ss.android.ugc.aweme:id/ibv", text="$orderBy").click()
        d(resourceId="com.ss.android.ugc.aweme:id/ibv", text="$publishTime").click()
        d(resourceId="com.ss.android.ugc.aweme:id/de8").click()
        d(resourceId="android:id/text1", text="视频").click()
        count = 0
        while count < 200:
            count = count + 1
            d.swipe(250, 1000, 250, 0, 0.01)
            if d(text="暂时没有更多了").exists(timeout=0.01):
                return True
        return True
    except Exception as e:
        utils.push.push_dingtalk_message(str(e))
        return False


if __name__ == '__main__':
    gundam_script()
