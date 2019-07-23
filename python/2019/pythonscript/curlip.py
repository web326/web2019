#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

data = ['192.168.7.86:9900','192.168.7.169:2222','192.168.7.115:22']
pings = os.popen('ping -n 1 192.168.7.125').readlines()
print(pings)
for item in data:
    pings = os.popen('ping -n 1 192.168.7.125').readlines()
    print(pings)
    tmpres = os.popen('curl %s' %(item)).readlines()
    print((item).encode(),":",tmpres)

print("Ping and Curl 测试")
