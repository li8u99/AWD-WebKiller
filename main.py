from rich.console import Console
from core.data import banner
from lib.scan import alivescan
from lib.ssh import sshscan
from lib.getflag import submit_flag, getflag_raw
from lib.admin import admin_login


if __name__ == '__main__':
    console = Console()
    console.print(banner, style="bold green")
    parse_num = input("> ")
    if parse_num == "1": # 存活探测
        target_ip = input("扫描IP网段> ")
        target_suffix = input("扫描后缀，默认为空> ")
        alivescan(target_ip, target_suffix)
    elif parse_num == "2": # SSH攻击
        ssh_username = input("输入账号> ")
        ssh_password = input("输入密码> ")
        ssh_port = input("输入端口> ")
        ssh_cmd = input("输入命令(快捷键 1.修改密码，2.cat /flag)>")
        sshscan(ssh_username, ssh_password, ssh_cmd, ssh_port)
    elif parse_num == "3": # Web攻击
        submit_flag()
        # function_num = input("1. GET重放 2. Brupsuite Raw包重放 >")
        # if function_num == "1":
        #     submit_flag()
        # elif function_num == "2":
        #     getflag_raw()
    elif parse_num == "4": #登录框批量登录
        admin_login()
    #elif parse_num == "5": # 登录框改密码
