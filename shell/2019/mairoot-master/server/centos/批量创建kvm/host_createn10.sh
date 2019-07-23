#!/bin/bash

# 1.链接克隆
link_create ()
{
read -p "请输入要创建的虚拟机个数：" N
virsh snapshot-create-as base snap1
chattr +i /var/lib/libvirt/images/base.img 
chattr +i /etc/libvirt/qemu/base.xml
for i in `seq -f"%02g" 1 $N`
do
        qemu-img create -f qcow2 -b /var/lib/libvirt/images/base.img /var/lib/libvirt/images/n$i.img &
sleep 5s
virsh dumpxml base > /etc/libvirt/qemu/n$i.xml
sed -i 's/base/n'$i'/' /etc/libvirt/qemu/n$i.xml
sed -i '/uuid/d' /etc/libvirt/qemu/n$i.xml
sed -i '/mac address/d' /etc/libvirt/qemu/n$i.xml
virsh define /etc/libvirt/qemu/n$i.xml
virsh snapshot-create-as n$i snap1
done
chattr -i /var/lib/libvirt/images/base.img
}

# 2.完全克隆
all_create ()
{
read -p "请输入要创建的虚拟机个数：" M
for j in `seq -f"%02g" 1 $M`
do
        virt-clone -o base -n m$j -f /var/lib/libvirt/images/m$j.img &
        sleep 60s
virsh snapshot-create-as m$j snap1
done
}


  echo "Please Input a NUM(1-2): "
  read NUM
echo "1 is link_create kvm,2 is all_create kvm."
case "$NUM" in
1)link_create;;
2)all_create;;
*) echo "Please Input a NUM(1-2)";;
esac
