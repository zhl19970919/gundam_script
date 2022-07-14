import json
import os
import sys
import time
import traceback

import requests
import uiautomator2 as u2


def push_dingtalk_message(msg: str):
    url = 'https://oapi.dingtalk.com/robot/send?access_token' \
          '=e0e3db9ead607b36ddc1a16ab6fcfaa98d29a9bff31b3f43aca2bfcfbd72f57a '
    header = {
        "Content-Type": "application/json"
    }
    data = {
        "msgtype": "text",
        "text": {
            "content": f"ActorError:{msg}, ActorFileName:{os.path.basename(__file__)}"
        }
    }
    res = requests.post(url=url, headers=header, data=json.dumps(data)).json()
    print(res)

# 仅适用于抖音18.5.0其他版本未测试xpath

def gundam_script() -> bool:
    # d = u2.connect('{equipment}')
    try:
        d = u2.connect("25cb279e")
        d.press("home")
        d.app_stop("com.ss.android.ugc.aweme")
        d.app_start("com.ss.android.ugc.aweme")
        with d.watch_context() as ctx:
            ctx.when("^(DENY|拒绝)").when("(允许|ALLOW)").click()
            ctx.when("同意").click()
            ctx.when("确定").click()
            ctx.wait_stable()
        d(resourceId="com.ss.android.ugc.aweme:id/e5r").click()
        d(focused=True).set_text("厨房神器")
        d.send_action("search")
        d(resourceId="com.ss.android.ugc.aweme:id/de8").click()
        d(resourceId="com.ss.android.ugc.aweme:id/ibv", text="最多点赞").click()
        d(resourceId="com.ss.android.ugc.aweme:id/ibv", text="一天内").click()
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
        push_dingtalk_message(str(e))
        return False


if __name__ == '__main__':
    gundam_script()
