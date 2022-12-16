import requests
import re
from core.data import FLAG_REGEX, conf
import yaml


def repeat(target, data, mathod, header):
    if mathod == "POST":
        resp = requests.post(target,data=data, verify=False, timeout=5, headers=header)
        match = re.search(FLAG_REGEX, resp.text)
        return match.group()
    elif mathod == "GET":
        resp = requests.get(target, verify=False, timeout=5, headers=header)
        match = re.search(FLAG_REGEX, resp.text)
        return match.group()


# TODO
def upload_repeat(target,data,mathod):
    if mathod == "POST":
        resp = requests.post(target,data=data,verify=False,timeout=5)
        match = re.search(FLAG_REGEX, resp.text)
        return match.group()
    elif mathod == "GET":
        resp = requests.get(target,verify=False,timeout=5)
        match = re.search(FLAG_REGEX,resp.text)
        return match.group()


def _webtargetcheck(filename):
    with open(filename,'r') as f:
        targets_raw = f.readlines()
    mytargets = []
    for target in targets_raw:
        ip_port = target.split(":")
        if len(ip_port) == 2:  # 目标文件内包含端口
                port = ip_port[1]
        else:
            port = conf.port

        match = re.search(r"http://|https://",ip_port[0])
        if match:
            mytargets.append(ip_port[0]+":"+port)
        else:
            mytargets.append('http://'+":"+port)
    return mytargets


def _pwntargetcheck(filename):
    with open(filename,'r') as f:
        targets_raw = f.readlines()

    mytargets = []
    myports = []
    for target in targets_raw:
        ip_port = target.split(":")
        mytargets.append(ip_port[0])
        if len(ip_port) == 2:  # 目标文件内包含端口
                myports.append(int(ip_port[1]))
        else:
            myports.append(int(conf.port))

    return myports


def web_init():
    with open("conf.yaml",'r') as f:
        y = yaml.load(f, Loader=yaml.FullLoader)

    conf.port = int(y["web_port"])
    conf.targets = _webtargetcheck("web_targets.txt")
    conf.flag_regex = y["flag_regex"]
    conf.request = y["request"]
    conf.response = y["response"]
    conf.cookies = []
    conf.url = None


def pwn_init():
    with open("conf.yaml",'r') as f:
        y = yaml.load(f, Loader=yaml.FullLoader)

    conf.port = int(y["pwn_port"])
    conf.targets, conf.ports = _pwntargetcheck("pwn_targets.txt")
    return
