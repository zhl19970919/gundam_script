import json
import os

import requests


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
