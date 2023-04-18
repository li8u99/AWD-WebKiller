import requests
import re
from core.data import FLAG_REGEX
def submit_flag(flag):  #提交flag输出提交结果
    z = re.search(FLAG_REGEX, flag)
    flag = z.group()
    if flag:
        flag = flag.rstrip('\n')
        submit_url = "http://10.1.10.10/event/25/awd/flag/?token=bf8e41596da7c230&flag={}".format(flag)
        header = {
            #"Content-Type": "application/x-www-form-urlencoded",
            #"token": ""
            #"Cookie": ""
        }
        flag = flag.rstrip('\n')
        data = "flag={}&token=".format(flag)
        r = requests.get(submit_url, headers=header, timeout=1)
        #r = requests.post(submit_url, headers=header, data=data, timeout=1)
        print(r.text)
    else:
        print("未匹配到FLAG  @！@")

