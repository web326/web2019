#!/bin/bash  
 # nc -v -w 10 -z 192.168.200.101 5555 （nc命令用法）
#-v 显示指令执行过程。
#-w <超时秒数> 设置等待连线的时间。
#-u 表示使用UDP协议
#-z 使用0输入/输出模式，只在扫描通信端口时使用
cat ip.txt | while read line
do
  nc -w 5 -z $line > /dev/null 2>&1
  if [ $? -eq 0 ]
  then
    echo -e "\033[32m $line:通 \033[0m"
  else
    echo -e "\033[31m $line:不通 \033[0m"
  fi
done
