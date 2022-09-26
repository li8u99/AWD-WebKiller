import requests
import re
from core.data import FLAG_REGEX,conf
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


def _targetcheck(filename):
    with open(filename,'r') as f:
        targets_raw = f.readlines()
    mytargets = []
    for target in targets_raw:
        match = re.search(r"http://|https://",target)
        if match:
            mytargets.append(target)
        else:
            mytargets.append('http://'+target)
    return mytargets


def init():
    with open("conf.yaml",'r') as f:
        y = yaml.load(f, Loader=yaml.FullLoader)

    conf.targets = _targetcheck("targets.txt")
    conf.flag_regex = y["flag_regex"]
    conf.request = y["request"]
    conf.response = y["response"]
    conf.cookies = []
    conf.url = None


init()