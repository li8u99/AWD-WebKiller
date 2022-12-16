import requests
from concurrent.futures import ThreadPoolExecutor
from core.data import IP_REGEX
import re


def _scantask(url):
    try:
        resp = requests.get(url, timeout=2)
        if resp:
            print(url)
            return url
    except Exception as e:
        pass


def alivescan(ip, suffix=None):
    targets = []
    results = []
    match = re.match(IP_REGEX, ip)
    ip_prefix = match.group()
    if suffix:
        for i in range(1, 255):
            targets.append('http://'+ip_prefix+str(i)+suffix)
    else:
        for i in range(1, 255):
            targets.append('http://'+ip_prefix+str(i))

    with ThreadPoolExecutor(10) as executor:
        for result in executor.map(_scantask, targets):
            if result != None:
                results.append(result + "\n")
    with open('web_targets.txt', 'w') as f:
        f.writelines(results)
