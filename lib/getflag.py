from lib.parseburplog import parseburprequest
from core.common import repeat
from core.data import conf


def getflag_raw():
    header, url, data, mathod = parseburprequest(conf.request)
    for target in conf.targets:
        target = target.strip + conf.url
        result = repeat(target,data,mathod)
        print(result)


def getflag():
    for target in conf.targets:
        target = target.strip + conf.url
        result = repeat(target, None, "GET")
        print(result)
