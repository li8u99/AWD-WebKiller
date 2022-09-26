import re
from lib.parseburplog import parseburprequest
import requests
from core.data import conf
from concurrent.futures import ThreadPoolExecutor


def admin_repeat(target,header,data,mathod,resp_body):
    if mathod == "POST":
        resp = requests.post(target,headers=header,data=data,verify=False,timeout=5)
        if re.search(resp_body, resp.text):
            return header['Cookie']
        else:
            return None
    elif mathod == "GET":

        resp = requests.get(target,headers=header,verify=False,timeout=5)
        if re.search(resp_body, resp.text):
            return header['Cookie']
        else:
            return None


# def changepassword(target, cookie,header,data,mathod,resp_body):
#     header['Cookie'] = cookie
#     if mathod == "POST":
#         resp = requests.post(target,headers=header,data=data,verify=False,timeout=5)
#         if re.search(resp_body, resp.text):
#             return target+'\t修改密码成功'
#         else:
#             return target+'\tNo'
#     elif mathod == "GET":
#         resp = requests.get(target,headers=header,verify=False,timeout=5)
#         if re.search(resp_body, resp.text):
#             return target+'\t修改密码成功'
#         else:
#             return target+'\tNo'


# def tagetmaker(filename):
#     with open(filename,'r') as f:
#         targets_raw = f.readlines()
#     mytargets = []
#     for target in targets_raw:
#         match = re.search(r"http://|https://",target)
#         if match:
#             mytargets += [target]
#         else:
#             mytargets += ['http://'+target]
#     return mytargets


def admin_login():
    header, url, data, mathod = parseburprequest(conf.request)

    with ThreadPoolExecutor(max_workers=5) as executor:  # 创建5个线程的线程池，
        futures = {executor.submit(admin_repeat, target,header,data,mathod,conf.response)for target in conf.targets}
        for future in futures:
            conf.cookie = future.result()

    with open("targets_cookies.txt","w") as f:
        f.writelines(conf.cookie)


def admin_changepwd_repeat(target_cookie,header,data,mathod,resp_body):
    target,cookie = target_cookie
    if mathod == "POST":
        resp = requests.post(target, headers=header,cookies=cookie, data=data, verify=False, timeout=5)
        if re.search(resp_body, resp.text):
            return header['Cookie']
        else:
            return None
    elif mathod == "GET":
        resp = requests.get(target, headers=header, cookies=cookie,verify=False, timeout=5)
        if re.search(resp_body, resp.text):
            return header['Cookie']
        else:
            return None

def admin_changepwd():
    header, url, data, mathod = parseburprequest(conf.request)

    # 将target和cookie放入字典里方便迭代
    tar_cookie_dict = {}
    for i in range(0,len(conf.targets)):
        tar_cookie_dict[conf.targets[i]] = conf.cookie


    with ThreadPoolExecutor(max_workers=5) as executor:  # 创建5个线程的线程池，
        futures = {executor.submit(admin_changepwd_repeat, target_cookie, header, data, mathod, conf.response) for target_cookie in
                   tar_cookie_dict}
        for future in futures:
            conf.cookie = future.result()

    with open("targets_cookies.txt", "w") as f:
        f.writelines(conf.cookie)

# if __name__ == '__main__':
#     # 读取login burp raw请求和响应
#     header,url,data,mathod= parseburprequest(conf.request)
#     targets = tagetmaker("target.txt")
#
#     print('开始登录...下面是登录成功和cookie')
#     for i in range(0,len(targets)):
#         targets[i] = targets[i].strip('\n')
#         targets[i] += url
#
#     with ThreadPoolExecutor(max_workers=5) as executor:  # 创建5个线程的线程池，
#         futures = {executor.submit(admin_repeat, target,header,data,mathod,resp_body)for target in targets}
#         for future in futures:
#                 data = future.result()
#                 print(data[0]+'\t'+data[1])
#                 # 将登录成功的target和cookie写入文件
#                 if data[1] != 'No':
#                     match = re.search(r"http://\S+/|https://\S+/",data[0])
#                     login_result += [match.group().rstrip(r'/')+'\t'+data[1]+'\n']
#
#     login_result=[]
#     with ThreadPoolExecutor(max_workers=5) as executor:  # 创建5个线程的线程池，
#         future_dict = {executor.submit(admin_repeat, target,header,data,mathod,resp_body)for target in targets}
#         for future in as_completed(future_dict):
#                 data = future.result()
#                 print(data[0]+'\t'+data[1])
#                 # 将登录成功的target和cookie写入文件
#                 if data[1] != 'No':
#                     match = re.search(r"http://\S+/|https://\S+/",data[0])
#                     login_result += [match.group().rstrip(r'/')+'\t'+data[1]+'\n']
#
#     with open("login_result.txt","w") as f:
#         f.writelines(login_result)
#
#     try:
#         with open("login_result.txt", "r") as f:
#             _ = f.readlines()
#         # 读取登录成功的target和cookie
#     except:
#         print("无法成功登录一台服务器，请手工测试")
#     chps_targets = []
#     chps_cookies = []
#     for line in _:
#         chps_target, chps_cookie = line.split('\t', 1)
#         chps_targets += [chps_target.strip('\n')]
#         chps_cookies += [chps_cookie.strip('\n')]
#
#     try:
#         with open("chpasswd_request.txt", 'r') as f:
#             requestlist = f.readlines()
#     except:
#         print("chpasswd_request.txt文件不存在，放弃执行修改密码操作")
#
#     header, url, data, mathod = parseburprequest(requestlist)
#     # 拼接url
#     for i in range(0,len(targets)):
#         targets[i] = targets[i].strip('\n')
#         targets[i] += url
#
#     with open('chpasswd_respose_body.txt', 'r', encoding='utf-8') as f:
#         resp_body = ''.join(f.readlines())
#
#     print("开始修改密码...")
#     with ThreadPoolExecutor(max_workers=5) as executor:
#         futures = []
#         for i in range(0,len(chps_targets)):
#             future = executor.submit(changepassword, chps_targets[i], chps_cookies[i],header, data, mathod, resp_body)
#             futures.append(future)
#         for future in as_completed(futures):
#             print(future.result())
