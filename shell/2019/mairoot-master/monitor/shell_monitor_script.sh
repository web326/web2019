#!/bin/bash

# Create for mai
 # Copyright http://www.mairoot.com
 # Create date 2018-07-21
 # Using check host source
 # Noting delete content
 # Shell Option $@

# 01.获取主机资源
function sys_info()
{
 # 系统信息
 Date=`date +%Y-%m-%d`
 Date_time=`date "+%Y-%m-%d__%H:%M:%S"`
 Host_name=`hostname`
 IP_net_dev="eth0"
 IP_addr=`ifconfig $IP_net_dev|grep "inet"|awk -F" " '{print $2}'`
 # 主机资源
 Disk_rate_sys=`df -h|grep \/\$|awk -F" " '{ print $5 }'`
 Disk_rate_sys2=${Disk_rate_sys%%%}
 Disk_rate_data=`df -h|grep \/boot\$|awk -F" " '{ print $5 }'`
 Disk_rate_data2=${Disk_rate_data%%%}
 CPU_free=`vmstat |tail -1|awk -F" " '{print $15}'`
 Load_ave15=`uptime |awk '{ print $NF }'|awk -F" " '{ print $1 }'`
 Load_ave15_1=`expr $Load_ave15`
 Mem_Total_kb=`cat /proc/meminfo | grep "MemTotal"|awk -F":" '{print $2}'|awk '{print $1}'`
 Mem_Free_kb=`cat /proc/meminfo | grep "MemFree"|awk -F":" '{print $2}'|awk '{print $1}'`
 Mem_Total=`expr $Mem_Total_kb / 1024`
 Mem_Free=`expr $Mem_Free_kb / 1024`
 # 微信接口
 CropID='ww4730ead71a1818a6'
 Secret='y4CCI-4LoiWmuqs6A5kYRpEyzhUlCveKeQ_Ik_WeEW4'
 GURL="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=$CropID&corpsecret=$Secret" 
 Gtoken=$(/usr/bin/curl -s -G $GURL | awk -F\" '{print $10}')
 PURL="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=$Gtoken"
 To_User="mai"
 To_Party="2"
 Agent_ID="1000002"
 # 日志目录
 if [ ! -d "/tmp/logs_check" ]; then mkdir /tmp/logs_check; fi
 Logs_file='/tmp/logs_check'
 # 远程地址
 SSH_addr="host.mairoot.com:22"
 # 运行业务
 Project_mode="腾讯云"
}

# 02.主机资源磁盘、CPU、MEM、LOAD
# 2.1 判断根磁盘使用率超额
  #系统盘使用率
function sys_disk()
{
if [ $Disk_rate_sys2 -gt 60 ]
 then
  echo "$Date_time 磁盘使用率超额" >> $Logs_file/disk_rate.$Date.log
  /usr/bin/curl --data-ascii '{ "touser": "'${To_User}'", "toparty": "'${To_Party}'","msgtype": "text","agentid": "'${Agent_ID}'","text": {"content": "'获取时间：${Date_time}'\n'运行业务：${Project_mode}'\n'远程地址：${SSH_addr}'\n'内网地址：${IP_addr}'\n'主机名称：${Host_name}'\n'磁盘使用：目录/为${Disk_rate_sys}'"},"safe":"0"}' $PURL
 else
  echo "$Date_time 磁盘使用率良好：$Disk_rate_sys" >> $Logs_file/disk_rate.$Date.log
 fi

  #数据盘使用率
if [ $Disk_rate_data2 -gt 60 ]
 then
  echo "$Date_time 磁盘使用率超额" >> $Logs_file/disk_rate.$Date.log
  /usr/bin/curl --data-ascii '{ "touser": "'${To_User}'", "toparty": "'${To_Party}'","msgtype": "text","agentid": "'${Agent_ID}'","text": {"content": "'获取时间：${Date_time}'\n'运行业务：${Project_mode}'\n'远程地址：${SSH_addr}'\n'内网地址：${IP_addr}'\n'主机名称：${Host_name}'\n'磁盘使用：目录/data为${Disk_rate_data}'"},"safe":"0"}' $PURL
 else
  echo "$Date_time 磁盘使用率良好：$Disk_rate_data" >> $Logs_file/disk_rate.$Date.log
 fi
}

# 2.2 判断MEM使用
function sys_mem()
{
 if [ $Mem_Free_kb -lt 92160 ]
 then
  echo "$Date_time MEM空闲少于90M" >> $Logs_file/MEM_free.$Date.log
  /usr/bin/curl --data-ascii '{ "touser":  "'${To_User}'", "toparty": "'${To_Party}'","msgtype": "text","agentid": "'${Agent_ID}'","text": {"content": "'获取时间：${Date_time}'\n'运行业务：${Project_mode}'\n'远程地址：${SSH_addr}'\n'内网地址：${IP_addr}'\n'主机名称：${Host_name}'\n'内存总共：${Mem_Total}MB'\n'内存剩余：${Mem_Free}MB'"},"safe":"0"}' $PURL
 else
  echo "$Date_time MEM空闲良好：$Mem_Free" >> $Logs_file/MEM_free.$Date.log
 fi
}

# 2.3 判断CPU空闲值过低
function sys_cpu()
{
 if [ $CPU_free -lt 10 ]
 then
  echo "$Date_time CPU空闲率少于10%" >> $Logs_file/CPU_free.$Date.log
  /usr/bin/curl --data-ascii '{ "touser":  "'${To_User}'", "toparty": "'${To_Party}'","msgtype": "text","agentid": "'${Agent_ID}'","text": {"content": "'获取时间：${Date_time}'\n'运行业务：${Project_mode}'\n'远程地址：${SSH_addr}'\n'内网地址：${IP_addr}'\n'主机名称：${Host_name}'\n'CPU空闲：${CPU_free}%'"},"safe":"0"}' $PURL
 else
  echo "$Date_time CPU空闲率良好：$CPU_free%" >> $Logs_file/CPU_free.$Date.log
 fi
}

# 2.4 判断服务器15分钟负载过高
function sys_load()
{
 if [ `expr $Load_ave15_1 \> 0` -gt 1 ]
 then
  echo "$Date_time 服务器15分钟负载过高：$Load_ave15%" >> $Logs_file/Load_ave15.$Date.log
  /usr/bin/curl --data-ascii '{ "touser":  "'${To_User}'", "toparty": "'${To_Party}'","msgtype": "text","agentid": "'${Agent_ID}'","text": {"content": "'获取时间：${Date_time}'\n'运行业务：${Project_mode}'\n'远程地址：${SSH_addr}'\n'内网地址：${IP_addr}'\n'主机名称：${Host_name}'\n'主机负载：${Load_ave15}%'"},"safe":"0"}' $PURL
 else
  echo "$Date_time 服务器15分钟负载良好：$Load_ave15%" >> $Logs_file/Load_ave15.$Date.log
 fi
}

# 03.检查服务
# 3.1 检查docker服务存活
function docker_status()
{
ps -ef|grep docker |grep -v grep
if [ $? -eq 0 ]
then
        Date_time311=`date "+%Y-%m-%d__%H:%M:%S"`
        echo "$Date_time311:docker is up" >> $Logs_file/Docker_pro.$Date.log 
else
                Date_time312=`date "+%Y-%m-%d__%H:%M:%S"`
                echo "$Date_time312:Docker服务第一次停止" >> $Logs_file/docker.$Date.log
                /usr/bin/curl --data-ascii '{ "touser": "'${To_User}'", "toparty": "'${To_Party}'","msgtype": "text","agentid": "'${Agent_ID}'","text": {"content": "'获取时间：${Date_time312}'\n'运行业务：${Project_mode}'\n'远程地址：${SSH_addr}'\n'内网地址：${IP_addr}'\n'主机名称：${Host_name}'\n'发生事件：Docker第一次停止'"},"safe":"0"}' $PURL
        sudo service docker start
        Os_code=$?
        if [ $Os_code -eq 0 ]
        then
                Date_time313=`date "+%Y-%m-%d__%H:%M:%S"`
                echo "$Date_time313:Docker_rec is up" >> $Logs_file/docker.$Date.log 
                /usr/bin/curl --data-ascii '{ "touser":  "'${To_User}'", "toparty": "'${To_Party}'","msgtype": "text","agentid": "'${Agent_ID}'","text": {"content": "'获取时间：${Date_time313}'\n'运行业务：${Project_mode}'\n'远程地址：${SSH_addr}'\n'内网地址：${IP_addr}'\n'主机名称：${Host_name}'\n'发生事件：Docker服务恢复'"},"safe":"0"}' $PURL
        elif [ $Os_code -ne 0 ]
        then
                Date_time314=`date "+%Y-%m-%d__%H:%M:%S"`
                echo "$Date_time314:Docker重启失败" >> $Logs_file/docker.$Date.log
                /usr/bin/curl --data-ascii '{ "touser":  "'${To_User}'", "toparty": "'${To_Party}'","msgtype": "text","agentid": "'${Agent_ID}'","text": {"content": "'获取时间：${Date_time314}'\n'运行业务：${Project_mode}'\n'远程地址：${SSH_addr}'\n'内网地址：${IP_addr}'\n'主机名称：${Host_name}'\n'发生事件：Docker服务停止'"},"safe":"0"}' $PURL
        fi
fi
}

# 3.2 检查docker容器存活
 # docker Container_ID 自下向上
function docker_container()
{
#Container_ID_ALL=("a0f74059bf06" "92757ceb5d78" "7e43120cf9e7" "0a86062f0db0")
Container_ID_ALL=("a0f74059bf06" "92757ceb5d78")
#Container_ID_ALL="`docker ps -aq`"
for Container_ID in ${Container_ID_ALL[@]}
do
    Container_Name=`docker inspect -f='{{.Name}}' $(docker ps -a -q|grep $Container_ID)|awk -F"/" '{print $2}'`
    docker ps |grep $Container_ID
    if [ $? -eq 0 ]
    then
        Date_time321=`date "+%Y-%m-%d__%H:%M:%S"`
        echo "$Date_time321:$Container_Name is up" >> $Logs_file/Docker_Container.$Date.log 
    else
        docker start $Container_ID
        Os_code=$?
        if [ $Os_code -eq 0 ]
        then
                Date_time322=`date "+%Y-%m-%d__%H:%M:%S"`
                echo "$Date_time322:$Container_Name is up" >> $Logs_file/Docker_Container.$Date.log 
                /usr/bin/curl --data-ascii '{ "touser":  "'${To_User}'", "toparty": "'${To_Party}'","msgtype": "text","agentid": "'${Agent_ID}'","text": {"content": "'获取时间：${Date_time322}'\n'运行业务：${Project_mode}'\n'远程地址：${SSH_addr}'\n'内网地址：${IP_addr}'\n'主机名称：${Host_name}'\n'发生事件：${Container_Name}服务恢复'"},"safe":"0"}' $PURL
        elif [ $Os_code -ne 0 ]
        then
                Date_time323=`date "+%Y-%m-%d__%H:%M:%S"`
                echo "$Date_time323:$Container_Name重启失败" >> $Logs_file/Docker_Container.$Date.log
                /usr/bin/curl --data-ascii '{ "touser":  "'${To_User}'", "toparty": "'${To_Party}'","msgtype": "text","agentid": "'${Agent_ID}'","text": {"content": "'获取时间：${Date_time323}'\n'运行业务：${Project_mode}'\n'远程地址：${SSH_addr}'\n'内网地址：${IP_addr}'\n'主机名称：${Host_name}'\n'发生事件：${Container_Name}服务停止'"},"safe":"0"}' $PURL
        fi
    fi
done
}

# 3.3 检查系统服务存活
function sys_service()
{
 ##由服务判别
Service_Name_ALL=("sshd" "nginx")
for Service_Name in ${Service_Name_ALL[@]}
do
    sudo ps -ef|grep $Service_Name|grep -v grep &> /dev/null
    if [ $? -eq 0 ]
    then
        Date_time331=`date "+%Y-%m-%d__%H:%M:%S"`
        echo "$Date_time331:$Service_Name is up" >> $Logs_file/Service.$Date.log
    else
        sudo service $Service_Name start
        Os_code=$?
        if [ $Os_code -eq 0 ]
        then
            Date_time332=`date "+%Y-%m-%d__%H:%M:%S"`
            echo "$Date_time332:$Service_Name is up" >> $Logs_file/Service.$Date.log
                /usr/bin/curl --data-ascii '{ "touser":  "'${To_User}'", "toparty": "'${To_Party}'","msgtype": "text","agentid": "'${Agent_ID}'","text": {"content": "'获取时间：${Date_time332}'\n'运行业务：${Project_mode}'\n'远程地址：${SSH_addr}'\n'内网地址：${IP_addr}'\n'主机名称：${Host_name}'\n'发生事件：${Service_Name}服务恢复'"},"safe":"0"}' $PURL
        elif [ $Os_code -ne 0 ]
        then
            Date_time333=`date "+%Y-%m-%d__%H:%M:%S"`
            echo "$Date_time333:$Service_Name重启失败" >> $Logs_file/Service.$Date.log
                /usr/bin/curl --data-ascii '{ "touser":  "'${To_User}'", "toparty": "'${To_Party}'","msgtype": "text","agentid": "'${Agent_ID}'","text": {"content": "'获取时间：${Date_time333}'\n'运行业务：${Project_mode}'\n'远程地址：${SSH_addr}'\n'内网地址：${IP_addr}'\n'主机名称：${Host_name}'\n'发生事件：${Service_Name}服务停止'"},"safe":"0"}' $PURL
        fi
    fi
done

 ##由端口判别
Service_Name_Port_ALL=("nginx" "dockerd")
for Service_Name_Port in ${Service_Name_Port_ALL[@]}
do
    sudo netstat -tnlp|grep $Service_Name_Port
    if [ $? -eq 0 ]
    then
        Date_time331=`date "+%Y-%m-%d__%H:%M:%S"`
        echo "$Date_time331:$Service_Name_Port is up" >> $Logs_file/Service.$Date.log
    else
        sudo service $Service_Name_Port start
        Os_code=$?
        if [ $Os_code -eq 0 ]
        then
            Date_time332=`date "+%Y-%m-%d__%H:%M:%S"`
            echo "$Date_time332:$Service_Name_Port is up" >> $Logs_file/Service.$Date.log
                /usr/bin/curl --data-ascii '{ "touser":  "'${To_User}'", "toparty": "'${To_Party}'","msgtype": "text","agentid": "'${Agent_ID}'","text": {"content": "'获取时间：${Date_time332}'\n'运行业务：${Project_mode}'\n'远程地址：${SSH_addr}'\n'内网地址：${IP_addr}'\n'主机名称：${Host_name}'\n'发生事件：${Service_Name_Port}服务恢复'"},"safe":"0"}' $PURL
        else [ $Os_code -ne 0 ]
        then
            Date_time333=`date "+%Y-%m-%d__%H:%M:%S"`
            echo "$Date_time333:$Service_Name重启失败" >> $Logs_file/Service.$Date.log
                /usr/bin/curl --data-ascii '{ "touser":  "'${To_User}'", "toparty": "'${To_Party}'","msgtype": "text","agentid": "'${Agent_ID}'","text": {"content": "'获取时间：${Date_time333}'\n'运行业务：${Project_mode}'\n'远程地址：${SSH_addr}'\n'内网地址：${IP_addr}'\n'主机名称：${Host_name}'\n'发生事件：${Service_Name}服务停止'"},"safe":"0"}' $PURL
        fi
    fi
done
}

# 3.4 检查端口服务存活
 ##由端口判别
function web_front_end()
{
Service_Port_ALL=("8080" "2222")
for Service_Port in ${Service_Port_ALL[@]}
do
    sudo netstat -tnlp |grep $Service_Port
    Os_code=$?
    if [ $Os_code -eq 0 ]
    then
        Date_time341=`date "+%Y-%m-%d__%H:%M:%S"`
        echo "$Date_time341:$Service_Port is up" >> $Logs_file/Service.$Date.log
    elif [ $Os_code -ne 0 ]
        Date_time342=`date "+%Y-%m-%d__%H:%M:%S"`
        echo "$Date_time343:$Service_Port重启失败" >> $Logs_file/Service.$Date.log
        /usr/bin/curl --data-ascii '{ "touser":  "'${To_User}'", "toparty": "'${To_Party}'","msgtype": "text","agentid": "'${Agent_ID}'","text": {"content": "'获取时间：${Date_time342}'\n'运行业务：${Project_mode}'\n'远程地址：${SSH_addr}'\n'内网地址：${IP_addr}'\n'主机名称：${Host_name}'\n'发生事件：${Service_Port}服务停止'"},"safe":"0"}' $PURL
    fi
done
}

# 04.检查URL服务存活
function web_url()
{
Urls_all='麦子稻草：https://www.mairoot.com'
Urls=`echo $Urls_all|awk -F"：" '{print $2}'`
for Url in $Urls
    do
    Date_time441=`date "+%Y-%m-%d__%H:%M:%S"`
    echo $Url
    Url_Name=`echo $Urls_all|grep $Url$|awk -F"：" '{print $1}'`
    curl -I -s --retry 0 --retry-max-time 8 $Url|grep '^HTTP/1.1 [2|3]'
    Os_code=$?
    if [ $Os_code -eq 0 ]
    then
    echo "$Date_time441:$Url is OK" >> $Logs_file/Urls.$Date.log
    fi
    Web_Code=`curl -I -s --retry 0 --retry-max-time 8 $Url|grep '^HTTP/1.1 [4|5]'|awk '{print $2}'`
    echo $Web_Code|grep '[4|5]'
    Os_code=$?
    if [ $Os_code -eq 0 ]
    then
        echo "$Date_time141:$Url is DOWN,网页报错：$Web_Code。" >> $Logs_file/Urls.$Date.log
        /usr/bin/curl --data-ascii '{ "touser":  "'${To_User}'", "toparty": "'${To_Party}'","msgtype": "text","agentid": "'${Agent_ID}'","text": {"content": "'获取时间：${Date_time441}'\n'运行业务：${Project_mode}'\n'远程地址：${SSH_addr}'\n'内网地址：${IP_addr}'\n'主机名称：${Host_name}'\n'发生事件：${Url_Name}:${Url}不能访问'\n'网页报错：${Web_Code}'"},"safe":"0"}' $PURL
    fi
done
}

# 05.增加URL到文件
 # 使得百度自动收录
function add_url()
{
Seq_Num=`tail -1 /mairoot/www/wp/site.txt |awk -F'=' '{print $2}'`
Seq_Num_Start=`expr $Seq_Num_Start + 1`
Seq_Num_End=`expr $Seq_Num_Start + 100`
for i in `seq $Seq_Num_Start $Seq_Num_End`
do
    Url=https://www.mairoot.com/?p=$i
    curl -I -s --retry 0 --retry-max-time 8 $Url|grep '^HTTP/1.1 [2|3]'
    if [ $? -eq 0 ] ;then
        echo $Url |tee -a /mairoot/www/wp/site.txt
    fi
done
}

# 10 调用函数
function main()
{
#sys_info
#sys_disk
#sys_cpu
#sys_mem
#sys_load
#docker_status
#docker_container
#sys_service
#web_front_end
#web_url
#add_url
}
main
