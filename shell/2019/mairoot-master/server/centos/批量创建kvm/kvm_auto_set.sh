# !/bin/bash

# 1.关闭NetworkManager,selinux和防火墙
service NetworkManager stop &> /dev/null ; chkconfig NetworkManager off &> /dev/null
service iptables stop &> /dev/null ; chkconfig iptables off &> /dev/null

# 2.配置IP
rm -rf /etc/udev/rules.d/70-persistent-net.rules
start_udev &> /dev/null
Eth=eth0
IP=192.168.0.1$1
Mask=255.255.255.0
GW=192.168.0.254
DNS=202.96.134.133
cat > /etc/sysconfig/network-scripts/ifcfg-$Eth << END
DEVICE=$Eth
TYPE=Ethernet
ONBOOT=yes
BOOTPROTO=none
IPADDR=$IP
NETMASK=$Mask
GATEWAY=$GW
DNS1=$DNS
END
cat > /etc/sysconfig/network-scripts/ifcfg-eth1 << END
DEVICE=eth1
TYPE=Ethernet
ONBOOT=yes
BOOTPROTO=none
IPADDR=192.168.122.1$1
NETMASK=$Mask
END
service network restart &> /dev/null

# 3.修改主机名和主机名解析
cat > /etc/sysconfig/network << END
NETWORKING=yes
HOSTNAME=n0$1.mai.com
END
hostname n0$1
cat > /etc/hosts << END
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
192.168.122.11  n01.mai.com n01
192.168.122.12  n02.mai.com n02
192.168.122.13  n03.mai.com n03
192.168.122.14  n04.mai.com n04
192.168.122.15  n06.mai.com n05
192.168.122.16  n06.mai.com n06
192.168.122.17  n07.mai.com n07
192.168.122.18  n08.mai.com n08
192.168.122.19  n09.mai.com n09
192.168.122.20  n10.mai.com n10
192.168.0.11    n01.mai.com n01
192.168.0.12    n02.mai.com n02
192.168.0.13    n03.mai.com n03
192.168.0.14    n04.mai.com n04
192.168.0.15    n05.mai.com n05
192.168.0.16    n06.mai.com n06
192.168.0.17    n07.mai.com n07
192.168.0.18    n08.mai.com n08
192.168.0.19    n09.mai.com n09
192.168.0.20    n10.mai.com n10
END

# 4.配置yum源
rm -rf /etc/yum.repos.d/*
cat > /etc/yum.repos.d/yum.repo << END
[base]
name=mai
baseurl=ftp://192.168.122.1/pub/centos6/
enabled=1
gpgcheck=0
END
yum clean all &> /dev/null ; yum repolist &> /dev/null

# 5.安装基本软件
LANG=C
yum install -y vim openssh-clients rsync lftp &> /dev/null
service rpcbind restart &> /dev/null ; chkconfig rpcbind on &> /dev/null

# 6.SSH不对主机进行反向解析
echo "UseDNS no" >> /etc/ssh/sshd_config
service  sshd restart &> /dev/null ； chkconfig sshd on &> /dev/null

# 7.重启电脑
sed -r -i 's/id:[0-9]:initdefault:/id:3:initdefault:/' /etc/inittab
echo "1" | passwd --stdin root &> /dev/null
#rm -rf /etc/udev/rules.d/70-persistent-net.rules   #如果不行，则执行该句，并再次重启
:> /root/.bash_history
history -c
reboot
