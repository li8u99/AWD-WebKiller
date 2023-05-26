import requests
import re
from core.data import FLAG_REGEX
import time


def submit_flag(flag):  #提交flag输出提交结果
    z = re.search(FLAG_REGEX, flag)
    flag = z.group()
    if flag:
        flag = flag.rstrip('\n')
        submit_url = "http://10.10.10.100/api/v1/awd/answer?evt=da480abc-839b-4505-aca0-3410c12ca4c5"
        header = {
            "Content-Type": "application/x-www-form-urlencoded",
            #"token": "",
            "Cookie": ""
        }
        flag = flag.rstrip('\n')
        data = "flag={}&token=1333211310926581674".format(flag)
        #r = requests.get(submit_url, headers=header, timeout=1)
        r = requests.post(submit_url, headers=header, data=data, timeout=1)
        print(r.text)
        time.sleep(2)
    else:
        print("未匹配到FLAG  @！@")

