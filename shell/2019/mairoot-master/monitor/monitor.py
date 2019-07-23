#!/usr/bin/env python3
# coding=utf-8
# Create for mai
 # Copyright https://www.mairoot.com
 # Create date 2018-10-21

# 引入模块
import os, time, socket, requests, json, urllib.request, re
from collections import namedtuple
from collections import OrderedDict

# ------------------------通用信息--------------------------------
# 业务信息
run_project="test-all"
# 获取日期时间
get_date=time.strftime("%Y-%m-%d", time.localtime())
get_date_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# IP地址
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip
inside_net=get_host_ip()
outside_net="host.mairoot.com:2222"
# 主机名
host_name=socket.gethostname()
# 发生事件
hint_content="None"

# ------------------------磁盘信息--------------------------------
# 获取磁盘信息
disk_ntuple = namedtuple('partition', 'device mountpoint fstype')
usage_ntuple = namedtuple('usage', 'total used free percent')

# 获取所有磁盘设备
def disk_partitions(all=False):
    """Return all mountd partitions as a nametuple.
    If all == False return phyisical partitions only.
    """
    phydevs = []
    f = open("/proc/filesystems", "r")
    for line in f:
        if not line.startswith('none'):
            phydevs.append(line.strip())

        retlist = []
        f = open('/etc/mtab', "r")
        for line in f: 
            if not all and line.startswith('none'):
                continue
            fields = line.split()
            device = fields[0]
            mountpoint = fields[1]
            fstype = fields[2]
            if not all and fstype not in phydevs:
                continue
            if device == 'none':
                device = ''
            ntuple = disk_ntuple(device, mountpoint, fstype)
            retlist.append(ntuple)
        return retlist

# 统计磁盘使用情况
def disk_state(path):
    """Return disk usage associated with path."""
    st = os.statvfs(path)
    free = (st.f_bavail * st.f_frsize)
    total = (st.f_blocks * st.f_frsize)
    used = (st.f_blocks - st.f_bfree) * st.f_frsize
    try:
        percent = ret = (float(used) / total) * 100
    except ZeroDivisionError:
        percent = 0
    return usage_ntuple(round(total/1024/1024/1024, 3), round(used/1024/1024/1024, 3), round(free/1024/1024/1024, 3), round(percent, 3)) 

# ------------------------内存信息--------------------------------
def get_meminfo():
    ''' Return the information in /proc/meminfo as a dictionary '''
    meminfo=OrderedDict()
    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return meminfo

# ------------------------负载信息--------------------------------
def get_load():
    f = open("/proc/loadavg")
    loadstate=f.read().split() 
    return loadstate

# ------------------------CPU信息--------------------------------
def get_cpu_use():
    last_worktime=0
    last_idletime=0
    f=open("/proc/stat","r")
    line=""
    while not "cpu " in line: line=f.readline()
    f.close()
    spl=line.split(" ")
    worktime=int(spl[2])+int(spl[3])+int(spl[4])
    idletime=int(spl[5])
    dworktime=(worktime-last_worktime)
    didletime=(idletime-last_idletime)
    rate=float(dworktime)/(didletime+dworktime)
    cpu_t = rate*100
    last_worktime=worktime
    last_idletime=idletime
    if(last_worktime==0): return 0
    return cpu_t

# ------------------------发送信息--------------------------------
# 定义验证信息
ID="ww4730ead71a1818a6"  
Secret="y4CCI-4LoiWmuqs6A5kYRpEyzhUlCveKeQ_Ik_WeEW4"
UserID = "mai"
PartyID=1
AppID = 1000002

# 获取token
def get_token():
    gurl = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}".format(ID, Secret)
    r=requests.get(gurl)
    dict_result= (r.json())
    return dict_result['access_token']
def get_media_ID(path):
    Gtoken = get_token()
    img_url = "https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token={}&type=image".format(Gtoken)
    files = {'image': open(path, 'rb')}
    r = requests.post(img_url, files=files)
    re = json.loads(r.text)
    return re['media_id']

# 发送文本 
def  send_text(text): 
    post_data = {}
    msg_content = {}
    msg_content['content'] = text
    post_data['touser'] = UserID
    post_data['toparty'] = PartyID
    post_data['msgtype'] = 'text'
    post_data['agentid'] = AppID
    post_data['text'] = msg_content
    post_data['safe'] = '0'
    Gtoken = get_token()
    purl1="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(Gtoken)
    json_post_data = json.dumps(post_data,skipkeys=False,ensure_ascii=False)
    request_post = urllib.request.urlopen(purl1,json_post_data.encode(encoding='UTF8'))
    return request_post
    
# 发送图片 
def  send_tu(path):
    img_id = get_media_ID(path)
    post_data1 = {}
    msg_content1 = {}
    msg_content1['media_id'] = img_id
    post_data1['touser'] = UserID
    post_data1['toparty'] = PartyID
    post_data1['msgtype'] = 'image'
    post_data1['agentid'] = AppID
    post_data1['image'] = msg_content1
    post_data1['safe'] = '0'
    Gtoken = get_token()
    purl2="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(Gtoken)
    json_post_data1 = json.dumps(post_data1,False,False)
    request_post = urllib.request.urlopen(purl2,json_post_data1.encode(encoding='UTF8'))
    return request_post

def send_msg2wx(run_events="None", hint_content="None"):
    send_text2wx="获取时间:{};\n运行业务:{};\n远程地址:{};\n内网地址:{};\n主机名称:{};\n发生事件:{};\n提示内容:{}.".format(get_date_time, run_project, outside_net, inside_net, host_name, run_events, hint_content)
    send_text(send_text2wx)
    
# ------------------------修改内容--------------------------------
# 磁盘 -------------------
def disk_send_mgs():
    disk_paths=['/', '/boot', '/data']
    for disk_path in disk_paths:
        disk_new_state=disk_state(disk_path)
        disk_percent=float(disk_state(disk_path)[3])
        if disk_percent > 80:
            run_events="目录{}使用率为{}%".format(disk_path, disk_new_state[3])
            send_msg2wx(run_events)

# 内存 -------------------
def mem_send_mgs():
    get_run_meminfo=get_meminfo() #数据转换为list
    memtotal=format(get_run_meminfo['MemTotal'])
    memtotal=float(memtotal.split()[0])
    memfree=format(get_run_meminfo['MemFree'])
    memfree=float(memfree.split()[0])
    memswap=format(get_run_meminfo['SwapTotal'])
    memswap=float(memswap.split()[0])
    memswapfree=format(get_run_meminfo['SwapFree'])
    memswapfree=float(memswapfree.split()[0])
    mem_percent=round(((memtotal - memfree) / memtotal)*100, 1)
    memswap_percent=round(((memswap - memswapfree) / memswap)*100, 1)
    if mem_percent > 80:
        run_events="内存使用率超过{}%".format(mem_percent)
        send_msg2wx(run_events)
    if memswap_percent > 80:
        run_events="交换内存使用率超过{}%".format(memswap_percent)
        send_msg2wx(run_events)

# 负载 -------------------
def load_send_mgs():
    loadstate=get_load()
    loadstate1=loadstate[0]
    loadstate15=float(loadstate[2])
    if loadstate15 > 5:
        run_events="系统负载过高{}".format(loadstate15)
        send_msg2wx(run_events)

# CPU -------------------
def cpu_send_mgs():
    cpuuse_percent=round(get_cpu_use(),3)
    if cpuuse_percent > 80:
        run_events="CPU使用过高{}%".format(cpuuse_percent)
        send_msg2wx(run_events)

# ------------------------执行内容--------------------------------
# 运行main函数
if __name__=='__main__':
    disk_send_mgs()
    mem_send_mgs()
    load_send_mgs()
    cpu_send_mgs()