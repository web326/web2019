#创建一个host下的虚拟机：
# virt-install --name=base --ram=512 --vcpus=1 --disk /var/lib/libvirt/images/base.img,size=8,format=qcow2 --location /iso/CentOS-6.5-x86_64-bin-DVD1.iso -w bridge:br0,model=virtio -w network=default --force --autostart --extra-args="text console=tty0 console=ttyS0,115200"
