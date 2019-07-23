#!/usr/bin/env python
# -*-coding:utf-8-*-
import ssh

__author__ = "Allen Woo"

def connect_host(ip, port, username, password):
    '''
    连接远程主机
    '''
    client = ssh.SSHClient()
    client.set_missing_host_key_policy(ssh.AutoAddPolicy())
    try:
        client.connect(ip, port = port,
                       username = username,
                       password = password)
    except Exception,e:
        print e
        return False
    return client

# 连接远程服务器
client = connect_host(192.168.1.111,  22,  "test",  "123456")
# 文件下载
sftp = client.open_sftp()
remote_file = "/home/work/test.txt"
local_save_path = "/home/work/temp_file/text.txt"

sftp.get(remote_file, local_save_path)

# 文件上传差不多
remote_save_path = "/home/work/upload/test.txt"
local_file = "/home/work/text.txt"
sftp.put(local_file, remote_save_path)

# 命令执行
stdin, stdout, stderr = client.exec_command("ls -l ")
r = stdout.read()
print(r)

