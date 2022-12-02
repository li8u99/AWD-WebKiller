import requests


def submit_flag(flag):  #提交flag输出提交结果
    flag = flag.rstrip('\n')
    submit_url = "http://10.1.10.10/event/25/awd/flag/?token=bf8e41596da7c230&flag={}".format(flag)
    header = {
		#"Content-Type": "application/x-www-form-urlencoded",
		#"token": ""
	}
    flag = flag.rstrip('\n')
    data = "flag={}".format(flag)
    r = requests.get(submit_url, headers=header,timeout=1)# data=data)
    print(r.text)