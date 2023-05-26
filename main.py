#python3.11

from rich.console import Console
from core.data import banner
from lib.scan import alivescan
from lib.ssh import sshscan
from lib.web_flag import getflag, webshell

from lib.admin import admin_login
from lib.pwn_exp import *
from core.common import *
import sys


if __name__ == '__main__':

    console = Console()
    console.print(banner, style="bold green")
    parse_num = input("> ").strip()

    if parse_num == '1': # 存活探测
        target_ip = input("扫描IP网段:\n").strip()
        target_suffix = input("扫描后缀，默认为空\n").strip()
        alivescan(target_ip, target_suffix)

    elif parse_num == "2": # SSH攻击
        ssh_username = input("输入账号\n").strip()
        ssh_password = input("输入原密码\n").strip()
        ssh_new_password = input("输入要修改的密码\n").strip()
        ssh_port = input("输入端口\n").strip()
        ssh_cmd = input("输入命令:\n1.修改密码\n2.cat /flag\n").strip()
        sshscan(ssh_username, ssh_password, ssh_new_password, ssh_cmd, ssh_port)

    elif parse_num == "3": # Web攻击
        function_num = input("1.批量获取webshell\n2.批量获取并提交FLAG\n3.批量修改后台密码\n").strip()
        if function_num == "1":
            webshell()
        elif function_num == "2":
            getflag()
        elif function_num == "3":
            admin_login()

    elif parse_num == "4":  # Pwn攻击
        function_num = input("1.批量获取flag\n2. 批量getshell\n").strip()
        if function_num == "1":
            pwn_init()
            pwn_run()
        elif function_num == "2":
            pass
    else:
        print('输入序号错误')