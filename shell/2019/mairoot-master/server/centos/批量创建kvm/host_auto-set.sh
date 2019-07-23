#!/bin/bash
# 一、配置host机
# 1.关闭NetworkManager,selinux和防火墙
# 2.配置IP
# 3.修改主机名和主机名解析
# 4.配置yum源
# 5.安装基本软件
# 6.重启电脑

# 1.关闭NetworkManager,selinux和防火墙
service NetworkManager stop 2>&1 /dev/null ; chkconfig NetworkManager off
service iptables stop 2>&1 /dev/null ; chkconfig iptables off
sed -i s/SELINUX=.*/SELINUX=disabled/ /etc/selinux/config ; setenforce 0 2>&1 /dev/null

# 2.配置IP
Eth0_MAC=$(ifconfig -a | egrep 'eth[0-9]+' |awk '{print $NF}')
Eth=$(ifconfig -a |head -1 |cut -d" " -f1)
rm -rf /etc/udev/rules.d/70-persistent-net.rules
start_udev 2>&1 /dev/null

IP=192.168.0.251
Mask=255.255.255.0
GW=192.168.0.254
DNS=202.96.134.133
cat > /etc/sysconfig/network-scripts/ifcfg-$Eth << END
DEVICE=$Eth
TYPE=Ethernet
ONBOOT=yes
NM_CONTROLLED=none
BRIDGE=br0
END
cat > /etc/sysconfig/network-scripts/ifcfg-br0 << END
DEVICE=br0
TYPE=Bridge
ONBOOT=yes
BOOTPROTO=none
IPADDR=$IP
NETMASK=$Mask
GATEWAY=$GW
DNS1=$DNS
END
service network restart 2>&1 /dev/null

# 3.修改主机名和主机名解析
cat > /etc/sysconfig/network << END
NETWORKING=yes
HOSTNAME=h.mai.com
END
hostname h.mai.com
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
END

# 4.配置yum源
rm -rf /etc/yum.repos.d/*
cat > /etc/yum.repos.d/yum.repo << END
[base]
name=mai
baseurl=file:///yum
enabled=1
gpgcheck=0
END
mkdir -p /iso
wget ftp://192.168.0.254/CentOS-6.5-x86_64-bin-DVD1.iso -P /iso/
mkdir -p /yum
mount -o loop /iso/CentOS-6.5-x86_64-bin-DVD1.iso /yum &> /dev/null
yum clean all &> /dev/null ; yum list &> /dev/null

# 5.安装基本软件
LANG=C
yum groupinstall -y "Virtualization" "Virtualization Client" "Virtualization Platform" "Virtualization Tools" &> /dev/null
yum install -y qemu-kvm virt-manager libvirt &> /dev/null
service libvirtd restart 2>&1 /dev/null ; chkconfig libvirtd on

# 6.在host机上共享yum源
yum install -y vsftpd 2>&1 /dev/null
service vsftpd restart 2>&1 /dev/null ; chkconfig vsftpd on 2>&1 /dev/null
mkdir -p /var/ftp/pub/centos6 2>&1 /dev/null
echo "/bin/mount -o loop /iso/CentOS-6.5-x86_64-bin-DVD1.iso /yum/" >> /etc/rc.local
echo "/bin/mount -o loop /iso/CentOS-6.5-x86_64-bin-DVD1.iso /var/ftp/pub/centos6/" >> /etc/rc.local
source /etc/rc.local

# 7.移植安装base虚拟机
wget ftp://192.168.0.254/base_for_centos6.5.zip -P /iso/
unzip /iso/base_for_centos6.5.zip -d /iso
mv /iso/base_for_centos6.5/base.img /var/lib/libvirt/images/
mv /iso/base_for_centos6.5/base.xml /etc/libvirt/qemu
virsh define /etc/libvirt/qemu/base.xml
# 7.重启电脑
sed -r -i 's/id:[0-9]:initdefault:/id:5:initdefault:/' /etc/inittab
echo "1" | passwd --stdin root >/dev/null
service iptables stop 2>&1 /dev/null ; chkconfig iptables off
:> /root/.bash_history
history -c
#reboot
